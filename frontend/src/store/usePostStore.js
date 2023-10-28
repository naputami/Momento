import {defineStore} from 'pinia';
import {reactive} from 'vue';

export const usePostStore = defineStore('post', ()=> {

    const postState = reactive({
        posts: [],
        currentPage: 1,
        totalPage: null,
        cachedPages: {}
    });

    const setPosts = (posts) => {
        postState.posts = postState.posts.concat(posts);

    };

    const setNewPost = (post) => {
        postState.posts = [post, ...postState.posts]
    }

    const setDeletedPost = (id) => {
        postState.posts = postState.posts.filter(post => post.id !== id)
    }
    
    const setCurrentPage = (page) => {
        postState.currentPage = page;
    };

    const cachePage = (page, data) => {
        postState.cachedPages[page] = data;
    }

    const setTotalPage = (number) => {
        postState.totalPage = number
    }

    const setUpdatedPost = (post) => {
        postState.posts = postState.posts.map(item => item.id === post.id ? post : item);
    }


    const removePostData = () => {
       postState.posts = [];
       postState.cachedPages = {};
       postState.currentPage = 1;
       postState.totalPage = null;
    };

    return {
        postState,
        setPosts,
        removePostData,
        setCurrentPage,
        cachePage,
        setTotalPage,
        setNewPost,
        setDeletedPost,
        setUpdatedPost
    };

});