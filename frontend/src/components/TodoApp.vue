<template>
  <div class="container">
    <h2 class="text-center mt-5">Hello TodoApp {{msg}}</h2>

    <!-- INPUT -->
    <div class="d-flex">
      <input v-model="task" type="text" placeholder="Enter Task." class="form-control">
      <button @click="submitTask" class="btn btn-warning rounded-0">SUBMIT</button>
      <!-- </input> -->
    </div>

    <!-- TASK TABLE -->
    <table class="table table-bordered mt-5">
      <thead>
        <tr>
          <th scope="col">Task</th>
          <th scope="col">Status</th>
          <th scope="col" class="text-center">#</th>
          <th scope="col" class="text-center">#</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(task,index) in array_of_tasks" :key="index">
          <th>
            <span :class="{'text-decoration-line-through': task.status === 'Finished'}">{{task.name}}</span>
          </th>
          <td style="width: 120px">
            <span class="pointer" :class="{
            'text-danger': task.status === 'To-do',
            'text-warning': task.status === 'In-progress',
            'text-success': task.status === 'Finished',
            }" @click="changeStatus(index)">{{task.status}}</span>
          </td>
          <td>
            <div class="text-center" :class="['pointer']" @click="editTodo(index)">
              <div>
                <span class="fa fa-pen"> </span>
              </div>
            </div>
          </td>
          <td>
            <div class="text-center" :class="['pointer']" @click="deleteTodo(index)">
              <span class="fa fa-trash"> </span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>



<script>

export default {
  data() {
    return {
      task: '',
      editedTask: null,
      availableStatuses: ["To-do", "In-progress", "Finished"],
      array_of_tasks: [
        {
          name: 'Go to the gym',
          status: 'To-do',
        },
        {
          name: 'Clean the house',
          status: 'In-progress',
        }
      ],
      msg: String
    }
  },

  methods: {
    submitTask() {
      if (this.task.length === 0) {
        return
      }

      if (this.editedTask === null) {
        this.array_of_tasks.push(
          {
            name: this.task,
            status: 'To-do'
          }
        )
      } else {
        this.array_of_tasks[this.editedTask].name = this.task
        this.editedTask = null
      }

      this.task = ''
    },
    deleteTodo(index) {
      this.array_of_tasks.splice(index, 1)
    },
    editTodo(index) {
      this.task = this.array_of_tasks[index].name
      this.editedTask = index
    },
    changeStatus(index) {
      let newIndex = this.availableStatuses.indexOf(this.array_of_tasks[index].status)
      if (newIndex == 2) {
        newIndex = 0
      } else {
        newIndex++
      }
      this.array_of_tasks[index].status = this.availableStatuses[newIndex]
    },
    // updateBackend() {
    //   console.log(JSON.stringify(this.array_of_tasks))
    // }
  },

  // created() {
  //   // Simple GET request using axios
  //   axios.get("http://localhost:80/api/get/todos/list")
  //     .then(response => this.msg = response.data);
  // }
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>