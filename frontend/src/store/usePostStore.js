import {defineStore} from 'pinia';
import {reactive} from 'vue';

export const usePostStore = defineStore('post', ()=> {

    const postState = reactive({
        posts: [],
        currentPage: 1,
        totalItems: null,
        cachedPages: {}
    });

    const setPosts = (posts) => {
        const concatedPosts = postState.posts.concat(posts);
        const set = new Set();
        const uniquePosts = [];
        
        for(const post of concatedPosts){
            const postString = JSON.stringify(post);

            if(!set.has(postString)){
                set.add(postString);
                uniquePosts.push(JSON.parse(postString))
            }

        }
        postState.posts = uniquePosts;

    };

    const setNewPost = (post) => {
        postState.posts = [post, ...postState.posts]
    }

    const setDeletedPost = (id) => {
        postState.posts = postState.posts.filter(post => post.id !== id)
    }
    
    const cachePage = (page, data) => {
        postState.cachedPages[page] = data;
    }

    const setTotalItems = (number) => {
        postState.totalItems = number
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
        cachePage,
        setTotalItems,
        setNewPost,
        setDeletedPost,
        setUpdatedPost,
    };

});