<template>
  <div class="container">
    <h2 class="text-center mt-5">MicroServices TodoApp</h2>

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
            }" @click="changeStatus(task.id)">{{task.status}}</span>
          </td>
          <td>
            <div class="text-center" :class="['pointer']" @click="editTodo(task.id)">
              <div>
                <span class="fa fa-pen"> </span>
              </div>
            </div>
          </td>
          <td>
            <div class="text-center" :class="['pointer']" @click="deleteTodo(task.id)">
              <span class="fa fa-trash"> </span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>



<script>
import axios from 'axios';
export default {
  data() {
    return {
      task: '',
      editedTask: null,
      editedTaskStatus: null,
      availableStatuses: ["To-do", "In-progress", "Finished"],
      array_of_tasks: [],
    }
  },

  methods: {
    async submitTask() {
      if (this.task.length === 0) {
        return
      }

      if (this.editedTask === null) {
        try {
          const response = await axios.post('http://localhost:80/api/create/todo', {
            "name": this.task, "status": "To-do"
          });
          console.log(response);
        } catch (error) {
          console.log(error.response);
        }
      } else {
        await axios.post(`http://localhost:80/api/update/todo/${this.editedTask}`, {
          "name": this.task, "status": this.editedTaskStatus
        })
        this.editedTask = null
        this.editedTaskStatus = null
      }

      this.task = ''
      this.refreshView()
    },
    async deleteTodo(index) {
      await axios.post(`http://localhost:80/api/delete/todo/${index}`);
      this.refreshView()
    },
    async editTodo(index) {
      var todo_object = this.getTodoObject(index)
      this.task = todo_object.name
      this.editedTask = todo_object.id
      this.editedTaskStatus = todo_object.status
    },
    async changeStatus(index) {
      var todo_object = this.getTodoObject(index)
      let newIndex = this.availableStatuses.indexOf(todo_object.status)
      if (newIndex == 2) {
        newIndex = 0
      } else {
        newIndex++
      }
      await axios.post(`http://localhost:80/api/update/todo/${todo_object.id}`, { "name": todo_object.name, "status": this.availableStatuses[newIndex] });
      this.refreshView()
    },
    async refreshView() {
      const response = await axios.get('http://localhost:80/api/get/todos/list');
      this.array_of_tasks = response.data;
    },
    async getTodoObject(index) {
      var todo_object = this.array_of_tasks.filter(obj => {
        return obj.id === index
      })
      return todo_object[0]
    }
  },

  async created() {
    this.refreshView()
  }
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
</style>