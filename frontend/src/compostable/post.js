import { ref } from 'vue';
import postApi from '../services/postApi';

export const useFetch = () => {
    const success = ref(null);
    const error = ref(null);
    const data = ref([]);
    const totalPage = ref(null);

    const fetchPosts = async (url) => {
        try {
            const response = await postApi.get(url);
            data.value = response.data.posts;
            success.value = response.data.success;
            totalPage.value = response.data.total_page;
            console.log('this is response total page value', totalPage.value)
        } catch(err) {
            error.value = err;
            console.log(err)

        }
    }

    const postTextOnly = async (url, content) => {
        try {
            const response = await postApi.post(url, content);
            data.value = response.data.post;
            success.value = response.data.success;
        } catch (err) {
            error.value = err;
            console.log(error)
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
        } catch (err) {
            error.value = err;
            console.log(error)
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
        } catch(err) {
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
        totalPage, 
        deletePost,
        likePost,
        dislikePost
    }


}