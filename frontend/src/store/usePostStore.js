import {defineStore} from 'pinia';
import {ref, computed} from 'vue';
import postApi from '../services/postApi';

export const usePostStore = defineStore('post', ()=> {

    const postState = ref([]);


    const getPosts = async () => {
        try {
            const response = await postApi.get('api/posts');
            postState.value = response.data.posts;
        } catch (err) {
            console.log('Something wrong!');
            console.log(err)
        }
        
    };

    const addTextOnlyPost = async (data) => {
        try {
            const response = await postApi.post('api/posts', data);
            postState.value = postState.value.concat(response.data.post);

        } catch(err) {
            console.log(err);
        }
    };

    const addWithImagePost = async (data) => {
        try{
            const response = await postApi.post('api/posts', data, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            postState.value = postState.value.concat(response.data.post);
        } catch(err) {
            console.log(err);
        }

    };

    const deletePost = async (id) => {
        try {
            const response = await postApi.delete(`api/posts/${id}`);
            postState.value = postState.value.filter(post => post.id !== id);
        } catch(err) {
            console.log("Something wrong", err);
        }
    }
    
    const likePost = async (id) => {
        try {
            const response = await postApi.post(`api/posts/${id}/like`, null);
            postState.value = postState.value.map(item => item.id === id ? response.data.post : item);
        } catch(err) {
            console.log("Something wrong", err);
        }
    }

    const dislikePost = async (id) => {
        try {
            const response = await postApi.post(`api/posts/${id}/dislike`, null);
            postState.value = postState.value.map(item => item.id === id? response.data.post : item);
        } catch(err) {
            console.log("Something wrong", err)
        }
    };

    const removePostData = () => {
        postState.value = [];
    };

    return {
        postState,
        getPosts,
        addTextOnlyPost,
        addWithImagePost,
        deletePost,
        likePost,
        dislikePost,
        removePostData
    };

});