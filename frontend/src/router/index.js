import { createRouter, createWebHistory } from 'vue-router';
import FrontPageView from '../views/FrontPageView.vue';
import { useAuthStore } from '../store/useAuthStore';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Front Page',
      component: FrontPageView,
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('../views/MainView.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/leaderboard',
      name: 'Leaderboard',
      component: () => import('../views/LeaderBoardView.vue'),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/signup',
      name: 'Sign Up',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/admin_signup',
      name: 'Admin Sign Up',
      component: () => import('../views/AdminRegisterView.vue')
    },
  ]
})

router.beforeEach((to, from, next) => {
  const {isAuthenticated } = useAuthStore();

  if(to.meta.requiresAuth) {
    if(isAuthenticated) {
      next();
    } else {
      next('/login')
    }
  } else {
    next()
  }

})

export default router
