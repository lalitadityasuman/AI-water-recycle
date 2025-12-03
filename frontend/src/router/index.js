import { createRouter, createWebHistory } from "vue-router";
import InputPage from "../pages/InputPage.vue";
import DashboardPage from "../pages/DashboardPage.vue";
import HistoryPage from "../pages/HistoryPage.vue";

const routes = [
  { path: "/", redirect: "/input" },
  { path: "/input", component: InputPage },
  { path: "/dashboard", component: DashboardPage },
  { path: "/history", component: HistoryPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
