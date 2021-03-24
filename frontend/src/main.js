import Vue from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import './index.css'

Vue.config.productionTip = false;

Vue.prototype.$apiUrl = `http://127.0.0.1:8000/api/`;
Vue.prototype.$http = axios.create({
  baseURL: Vue.prototype.$apiUrl,
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
