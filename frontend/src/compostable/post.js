import { ref } from 'vue';
import postApi from '../services/postApi';

export const useFetch = () => {
    const success = ref(null);
    const error = ref(null);
    const data = ref([]);
    const addedPost = ref(null);

    const fetchPosts = async (url) => {
        try {
            const response = await postApi.get(url);
            console.log(response.data)
            data.value = response.data.posts;
            success.value = response.data.success;
        } catch(err) {
            error.value = err;
            console.log(err)

        }
    }

    const postContent = async (url, content) => {
        try {
            const response = await postApi.post(url, content);
            data.value = data.value.concat(response.data.post);
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
            data.value = data.value.concat(response.data.post);
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


    return {
        fetchPosts,
        data,
        postContent,
        postFile,
        addedPost,
        fetchCountPosts
    }


}