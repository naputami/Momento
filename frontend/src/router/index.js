import { createRouter, createWebHistory } from 'vue-router';
// import LoginView from '../views/LoginView.vue'
// import RegisterView from '../views/RegisterView.vue'
import MainView from '../views/MainView.vue';
import { useAuthStore } from '../store/useAuthStore';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: MainView,
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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/signup',
      name: 'Sign Up',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/RegisterView.vue')
    }

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
