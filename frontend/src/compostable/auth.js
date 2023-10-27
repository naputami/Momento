/* eslint-disable no-unused-vars */
import { ref, reactive } from 'vue';
import axios from 'axios';
import postApi from '../services/postApi';

export const useAuth = () => {
    const success = ref(null);
    const error = ref(null);
    const accessToken = ref(null);
    const refreshToken = ref(null);
    const username = ref(null);
    const role = ref(null);

    const alertData = reactive({
        message: '',
        status: '',
    })

    const alertVisibility = ref(false);

    const hideAlert = () => {
        alertVisibility.value = false;
        success.value = null;
        error.value = null;
    }

    const userLogin = async (url, formData) => {
        try {
            axios.defaults.withCredentials = true;
            const response = await axios.post(url, formData);
            accessToken.value = response.data.accessToken;
            refreshToken.value = response.data.refreshToken;
            username.value = response.data.user.username;
            role.value = response.data.user.role;
            success.value = response.data.message;
        } catch(err){
            error.value = err.response.data.message;
            console.log(error.value)
        }
    }

    const userLogout = async (url) => {
        try {
            const response = await postApi.post(url, null);
            success.value = response.data.message;
        } catch(err) {
            error.value = err.response.data.message;
            console.log(error.value)
        }
    }

    const accountRegister = async (url, formData) => {
        try {
            const response = await axios.post(url, formData);
            console.log("this is response", response)
            success.value = response.data.message;
        } catch(err) {
            error.value = err.response.data.message;
            console.log(error)
        }
    }

    return {
        success,
        error,
        userLogin,
        accountRegister,
        alertData,
        hideAlert,
        alertVisibility,
        userLogout,
        accessToken,
        refreshToken,
        username,
        role
    }
} 