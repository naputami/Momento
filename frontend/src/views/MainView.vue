<template>
<v-app>
    <NavigationBar />

    <v-container class="pt-16">
        <h2 v-show="displayedPosts.length === 0" class="mt-10 heading">No Post Created!</h2>
        <div v-for="item in displayedPosts" :key="item.id">
            <PostItem :user="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" :id="item.id" :img_name="item.img_name" :img_path="item.img_path" />
        </div>
        <div class="text-center">
            <v-container>
            <v-row justify="center">
                <v-col cols="8">
                <v-container class="max-width">
                    <v-pagination
                    v-model="currentPage"
                    class="my-4"
                    :length="totalPage"
                    ></v-pagination>
                </v-container>
                </v-col>
            </v-row>
            </v-container>
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
import AddPost from "../components/AddPost.vue";
import PostItem from "../components/PostItem.vue";
import NavigationBar from "../components/NavigationBar.vue";
import { useFetch } from "../compostable/post"

const store = usePostStore();
const {postState} = storeToRefs(store);
const {setPosts, cachePage, setTotalItems} = store;
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
})


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

