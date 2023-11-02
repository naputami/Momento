import { ref } from 'vue';
import postApi from '../services/postApi';

export const useFetch = () => {
    const success = ref(null);
    const error = ref(null);
    const data = ref([]);
    const totalItem = ref(null);

    const fetchPosts = async (url) => {
        try {
            const response = await postApi.get(url);
            data.value = response.data.posts;
            success.value = response.data.success;
            totalItem.value = response.data.totalPosts;
            console.log('this is response total page value', totalItem.value)
        } catch(err) {
            error.value = err.response.data.message;
            console.log(err)

        }
    }

    const postTextOnly = async (url, content) => {
        try {
            const response = await postApi.post(url, content);
            data.value = response.data.post;
            success.value = response.data.success;
            totalItem.value = response.data.totalPosts;
            console.log('this is response total page value', totalItem.value)
        } catch (err) {
            error.value = err.response.data.error;
            console.log(err)
        }
    }

    const postFile = async (url, formData) => {
        try {
            const response = await postApi.post(url, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            data.value = response.data.post;
            success.value = response.data.success;
            totalItem.value = response.data.totalPosts;
            console.log('this is response total page value', totalItem.value)
        } catch (err) {
            error.value = err.response.data.error;;
            console.log(err)
        }
    }


    const fetchCountPosts = async () => {
        try {
            const response = await postApi.get('api/count_posts');
            data.value = response.data.data;
        } catch(err) {
            console.log("Something error", err);
        }
    }

    const deletePost = async (id) => {
        try {
            const response = await postApi.delete(`api/posts/${id}`);
            success.value = response.data.success;
            totalItem.value = response.data.totalPosts;
            console.log('this is response total page value', totalItem.value)
        } catch(err) {
            error.value = err.response.data.message;
            console.log("Something wrong", err);
        }
    }

    const likePost = async (id) => {
        try {
            const response = await postApi.post(`api/posts/${id}/like`, null);
            data.value = response.data.post;
        } catch(err) {
            console.log("Something wrong", err);
        }
    }

    const dislikePost = async (id) => {
        try {
            const response = await postApi.post(`api/posts/${id}/dislike`, null);
            data.value = response.data.post;
        } catch(err) {
            console.log("Something wrong", err)
        }
    };


    return {
        fetchPosts,
        data,
        postTextOnly,
        postFile,
        fetchCountPosts,
        totalItem, 
        deletePost,
        likePost,
        dislikePost,
        success,
        error
    }


}