<!-- eslint-disable no-unused-vars -->
<template>
     <v-card class="my-5 mx-auto pa-4" variant="elevated" :max-width="mdAndUp? '650': '500'">
    <v-card-text class="text-h5 py-2">
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
            <v-btn icon="$heartOutline" color="red"></v-btn>
            <span class="subheading me-2">{{ likes }}</span>
            <v-btn icon="$delete" @click="handleDeletePost(id)"></v-btn>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useDisplay } from 'vuetify';
import { usePostStore } from '../store/usePostStore';
const { mdAndUp } = useDisplay()
const {deletePost} = usePostStore()

const handleDeletePost = async (id) => {
  await deletePost(id)
}

const props = defineProps({
  user: String,
  likes: Number,
  content: String,
  created_at: String,
  id: String,
})
</script>