<!-- eslint-disable no-unused-vars -->
<template>
     <v-card class="my-5 mx-auto pa-4" variant="elevated" :max-width="mdAndUp? '650': '500'">
      <v-list-item class="w-100">
        <div class="d-flex justify-space-between">
              <div class="d-flex flex-row">
                <v-icon icon="$account" class="mr-2"></v-icon>
                <v-list-item-title>{{ user }}</v-list-item-title>
              </div>
              <v-list-item-subtitle>{{ formatDate(created_at) }}</v-list-item-subtitle>
          </div>
      </v-list-item>
      <v-divider color="primary"></v-divider>
    <v-card-text class="text-h5 pb-2 pt-3">
      <v-img
        :src="img_path"
        class="mb-5"
        width="w-100"
        :alt="img_name"
        v-show="img_path !== null"
      ></v-img>
      <span class="text-body-1">
        {{ content }}
      </span>
    </v-card-text>

    <v-card-actions class="pa-0">
      <v-list-item class="w-100 px-0">
          <div class="d-flex align-center">
            <v-btn :icon="liked? '$heart' : '$heartOutline'" color="red" @click="liked? handleDislikePost(id) : handleLikePost(id)"></v-btn>
            <span class="subheading me-2">{{ likes }}</span>
            <v-btn icon="$delete" @click="handleDeletePost(id)" v-show="user === username"></v-btn>
          </div>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useDisplay } from 'vuetify';
import { usePostStore } from '../store/usePostStore';
import { useAuthStore } from '../store/useAuthStore';
import { ref, onMounted } from 'vue';
import { useFetch } from '../compostable/post';
import { storeToRefs } from 'pinia';

const { mdAndUp } = useDisplay();
const { username } = useAuthStore();
const { deletePost, likePost, dislikePost, data } =useFetch();

const liked = ref(false)
const store = usePostStore();
const {postState} = storeToRefs(store);
const {setDeletedPost, setUpdatedPost} = store;


const handleDeletePost = async (id) => {
  await deletePost(id);
  setDeletedPost(id);
  console.log("post state after delete", postState.value.posts)
};

const handleLikePost = async (id) => {
  await likePost(id);
  setUpdatedPost(data.value);
  liked.value = true;
  localStorage.setItem(`liked_${id}`, 'true');
};

const handleDislikePost = async (id) => {
  await dislikePost(id);
  setUpdatedPost(data.value);
  liked.value = false;
  localStorage.setItem(`liked_${id}`, 'false');
};

onMounted(() => {
  const id = props.id;
  const storedValue = localStorage.getItem(`liked_${id}`);
  if (storedValue === 'true') {
    liked.value = true;
  }
  if (storedValue === 'false') {
    liked.value = false;
  }
});

const formatDate = (inputDate) => {
  const parsedDate = new Date(inputDate);

  const day = parsedDate.getDate() - 1;
  const month = parsedDate.getMonth() + 1; 
  const year = parsedDate.getFullYear();

  const formattedDate = `${String(day).padStart(2, '0')}/${String(month).padStart(2, '0')}/${year}`;

  return formattedDate;
}

const props = defineProps({
  user: String,
  likes: Number,
  content: String,
  created_at: String,
  id: String,
  img_name: String,
  img_path: String,
})
</script>