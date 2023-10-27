import {defineStore} from 'pinia';
import {ref, computed} from 'vue';

export const useAuthStore = defineStore('auth', () => {
    const accessToken = ref(null || localStorage.getItem("accessToken"));
    const refreshToken = ref(null || localStorage.getItem("refreshToken"));
    const username = ref(null || localStorage.getItem("username"));
    const role = ref(null || localStorage.getItem("role"));

    const isAuthenticated = computed(() => accessToken.value !== null);

    const isAdmin = computed(() => role.value === 'admin');

    const setToken = (access_token, refresh_token) => {
        localStorage.setItem("accessToken", access_token);
        localStorage.setItem("refreshToken", refresh_token);
         accessToken.value = access_token
         refreshToken.value = refresh_token
    }

    const setUserData = (user_name, user_role ) => {
        localStorage.setItem("username", user_name);
        localStorage.setItem("role", user_role);
        username.value = user_name;
        role.value = user_role;
    }

    const removeUserData = () => {
        localStorage.clear();
        username.value = null;
        role.value = null;
        accessToken.value = null;
        refreshToken.value = null;
    }
     
    return {
       accessToken, 
       refreshToken, 
       setToken, 
       isAuthenticated, 
       username,
       role,
       setUserData,
       removeUserData,
       isAdmin
    }
    
})