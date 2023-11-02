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
import Swal from 'sweetalert2';

const { mdAndUp } = useDisplay();
const { username } = useAuthStore();
const { deletePost, likePost, dislikePost, data, success, error, totalItem } =useFetch();

const liked = ref(false)
const store = usePostStore();
const {postState} = storeToRefs(store);
const {setDeletedPost, setUpdatedPost, setTotalItems} = store;


const handleDeletePost = async (id) => {
  Swal.fire({
        title: 'Delete Confirmation',
        text: 'Are you sure to delete this post?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#006d77ff',
        cancelButtonColor: '#cd858c',
        confirmButtonText: 'Yes',
  }).then(async result => {
      if(result.isConfirmed){
        await deletePost(id);
        if(success.value){
          setDeletedPost(id);
          setTotalItems(totalItem.value)
          console.log("post state after delete", postState.value.posts);
          Swal.fire({
                      title: 'Deleting post successfully!',
                      icon: 'success',
                      showConfirmButton: false,
                      timer: 2000
                    })
          success.value = null;
        }

        if(error.value){
          console.log(error.value)
          Swal.fire({
                        title: 'Deleting Post Failed!',
                        text: `${error.value}`,
                        icon: 'error',
                        showConfirmButton: false,
                        timer: 3000
                    })
        }
        error.value = null;
      }
     
  })
 
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

  const formattedDate =parsedDate.toLocaleDateString('id-ID');

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