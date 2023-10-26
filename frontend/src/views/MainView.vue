<template>
<v-app>
    <NavigationBar />

    <v-container class="pt-16">
        <div v-for="item in postState" :key="item.id">
            <PostItem v-if="item.img_path === null" :user="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" :id="item.id" />
            <PostItemWithImage v-else :username="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" :img_name="item.img_name" :img_path="item.img_path" :id="item.id" />

        </div>
    </v-container>
    <VLayoutItem model-value position="bottom" class="text-end" size="88">
        <div class="ma-4">
            <AddPost />
        </div>
    </VLayoutItem>
</v-app>
</template>

<script setup>
import { usePostStore } from "../store/usePostStore";
import { storeToRefs } from "pinia";
import AddPost from "../components/AddPost.vue";
import PostItem from "../components/PostItem.vue";
import NavigationBar from "../components/NavigationBar.vue"
import PostItemWithImage from "../components/PostItemWithImage.vue"
import { onMounted } from "vue";

const store = usePostStore();
const {postState} = storeToRefs(store);
const {getPosts} = store;

onMounted(async () => {
    await getPosts();
    console.log('poststate', postState)
})




</script>

<style scoped></style>