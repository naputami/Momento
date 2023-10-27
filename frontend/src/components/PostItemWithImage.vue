<template>
    <v-card class="my-5 mx-auto pa-4" variant="elevated" :max-width="mdAndUp? '650': '500'">
    <v-card-text class="text-h5 py-2">
      <v-img
        :src="img_path"
        class="mb-5"
        width="w-100"
        :alt="img_name"
      ></v-img>
      <span class="text-body-1">
        {{ content }}
      </span>
    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <template v-slot:prepend>
          <v-icon icon="$account" class="mr-2"></v-icon>
          <div class="d-flex flex-column">
            <v-list-item-title>{{ user }}</v-list-item-title>
            <v-list-item-subtitle>{{ created_at }}</v-list-item-subtitle>
          </div>
        </template>

        <template v-slot:append>
          <div class="d-flex align-center">
            <v-btn :icon="liked? '$heart' : '$heartOutline'" color="red" @click="liked? handleDislikePost(id) : handleLikePost(id)"></v-btn>
            <span class="subheading me-2">{{ likes }}</span>
            <v-btn icon="$delete" @click="handleDeletePost(id)" v-show="user === username"></v-btn>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useDisplay } from 'vuetify';
import { ref, onMounted } from 'vue';
import { usePostStore } from '../store/usePostStore';
import { useAuthStore } from '../store/useAuthStore';

const {deletePost, likePost, dislikePost} = usePostStore();
const { mdAndUp } = useDisplay();
const liked = ref(false);
const { username } = useAuthStore();

const handleDeletePost = async (id) => {
  await deletePost(id)
}

const handleLikePost = async (id) => {
  await likePost(id);
  liked.value = true;
  localStorage.setItem(`liked_${id}`, 'true');
};

const handleDislikePost = async (id) => {
  await dislikePost(id);
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

const props = defineProps({
    content: String,
    img_name: String,
    img_path: String,
    user: String,
    likes: Number,
    created_at: String,
    id: String
})
</script>