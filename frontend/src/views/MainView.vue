<template>
<v-app>
    <NavigationBar />

    <v-container class="pt-16">
        <div v-for="item in dummyData" :key="item.id">
            <PostItem v-if="item.img_link === ''" :user="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" />
            <PostItemWithImage v-else :username="item.username" :likes="item.likes" :content="item.content" :created_at="item.created_at" :img_name="item.img_name" :img_path="item.img_link" />

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
import AddPost from "../components/AddPost.vue";
import PostItem from "../components/PostItem.vue";
import NavigationBar from "../components/NavigationBar.vue"
import PostItemWithImage from "../components/PostItemWithImage.vue"

const dummyData = [
    {
        content: "lorem ipsum dolor sir amet",
        username: "naputami",
        likes: 25, 
        id: 1,
        created_at: "22-03-2022",
        img_link: "../../public/ERD.jpg",
        img_name: "ERD"

    },
    {
        content: "lorem ipsum dolor sir amet",
        username: "naputami",
        likes: 25,
        id: 2,
        created_at: "22-03-2022",
        img_link: "",
        img_name: ""

    },
    {
        content: "lorem ipsum dolor sir amet",
        username: "naputami",
        likes: 25,
        id: 3,
        created_at: "22-03-2022",
        img_link: "",
        img_name: ""

    },
    {
        content: "lorem ipsum dolor sir amet",
        username: "naputami",
        likes: 25,
        created_at: "22-03-2022",
        id: 3,
        img_link: "../../public/ERD.jpg",
        img_name: "ERD"

    },
]
</script>

<style scoped></style>