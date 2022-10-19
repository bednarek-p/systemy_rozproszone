<template>
  <div class="container">
    <h2 class="text-center mt-5">Hello TodoApp {{msg}}</h2>

    <!-- INPUT -->
    <div class="d-flex">
      <input type="text" placeholder="Enter Task." class="form-control">
      <button class="byn byn-warning rounded-0">SUBMIT</button>
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
          <th>{{task.name}}</th>
          <td>{{task.status}}</td>
          <td>
            <div class=" text-center">
              <span class="fa fa-pen"> </span>
            </div>
          </td>
          <td>
            <div class="text-center">
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
      array_of_tasks: [
        {
          name: 'Go to the gym',
          status: 'to-do',
        },
        {
          name: 'Clean the house',
          status: 'in-progress',
        }
      ],
      msg: String
    }
  },

  created() {
    // Simple GET request using axios
    axios.get("http://localhost:80/api/get/todos/list")
      .then(response => this.msg = response.data);
  }
}
</script>
