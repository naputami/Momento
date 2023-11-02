<template>
<v-app>
    <NavigationBar />

    <v-container class="pt-16">
        <div v-for="item in displayedPosts" :key="item.id">
            <PostItem :user="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" :id="item.id" :img_name="item.img_name" :img_path="item.img_path" />
        </div>
        <div class="mt-8 text-center">
            <v-btn :prepend-icon="mdiChevronDoubleLeft" @click="changePage(-1)" :disabled="currentPage === 1" variant="elevated" color="primary">Previous</v-btn>
            <v-btn :append-icon="mdiChevronDoubleRight" @click="changePage(1)" :disabled="currentPage === totalPage" variant="elevated" color="primary" class="ml-2">Next</v-btn>
        </div>
    </v-container>
    <div class="fab">
        <AddPost />
    </div>
        
    </v-app>
</template>

<script setup>
import { ref, watch, computed, onMounted } from "vue";
import { usePostStore } from "../store/usePostStore";
import { storeToRefs } from "pinia";
import {mdiChevronDoubleRight, mdiChevronDoubleLeft} from '@mdi/js'
import AddPost from "../components/AddPost.vue";
import PostItem from "../components/PostItem.vue";
import NavigationBar from "../components/NavigationBar.vue";
import { useFetch } from "../compostable/post"

const store = usePostStore();
const {postState, uniquePosts} = storeToRefs(store);
const {setPosts, setCurrentPage, cachePage, setTotalItems} = store;
const { fetchPosts, data, totalItem} = useFetch()

const currentPage = ref(postState.value.currentPage);
const totalPage = computed(() => {
    return Math.ceil(postState.value.totalItems / 5)
})


onMounted(async () => {
    await fetchPosts(`api/posts?page=${currentPage.value}`);
    setPosts(data.value);
    cachePage(currentPage.value, data.value)
    setTotalItems(totalItem.value)
    console.log("this is unique post", uniquePosts)
})

const changePage = (pageChange) => {
      const newPage = currentPage.value + pageChange;
      if (newPage >= 1 && newPage <= totalPage.value) {
        currentPage.value = newPage;
        setCurrentPage(newPage);
        window.scrollTo(0,0)
      }
};

const fetchAnotherPagePost = async () => {
    try{
        const check = currentPage.value in postState.value.cachedPages

        if(!check){
            await fetchPosts(`api/posts?page=${currentPage.value}`)
            setPosts(data.value)
            setTotalItems(totalItem.value)
            cachePage(currentPage.value, data.value)
        }
    } catch (err) {
        console.log(err)
    }
}

const displayedPosts = computed(() => {
      const startIndex = (currentPage.value - 1) * 5;
       const endIndex = startIndex + 5;
      return postState.value.posts.slice(startIndex, endIndex);
    });


watch(currentPage, () => {
    fetchAnotherPagePost()
})



</script>
<style scoped>
.fab {
    position: fixed;
    right: 1rem;
    bottom: 3rem;
    width: max-content;
}

@media only screen and (min-width: 768px) {
    .fab {
        right: 5rem;
    }
}

@media only screen and (min-width: 992px) {
    .fab {
        right: 15rem;
    }
}
</style>

