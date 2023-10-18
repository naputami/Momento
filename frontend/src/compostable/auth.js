/* eslint-disable no-unused-vars */
import { ref, reactive } from 'vue';
import axios from 'axios';

export const useAuth = () => {
    const success = ref(null);
    const error = ref(null);

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
            const response = await axios.post(url, formData);
            success.value = response.data.message;
        } catch(err){
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
        alertVisibility
    }
} 