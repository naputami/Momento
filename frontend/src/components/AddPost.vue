<template>
      <v-btn @click="dialog = true" icon="$pencil" color="secondary" size="x-large"> </v-btn>

        <v-dialog v-model=dialog width="500">
                <v-card title="Add New Post">
                <v-divider></v-divider>
                <form width="w-100" class="mt-5 pa-5">
                    <v-file-input
                    chips
                    multiple
                    label="Add image (optional)"
                    variant="outlined"
                    prepend-icon="$camera"
                    ></v-file-input>
                    <v-textarea
                    label="Write your thougts here"
                    prepend-icon="$text"
                    variant="outlined"
                    ></v-textarea>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text="Cancel" @click="dialog = false"></v-btn>
                    <v-btn variant="tonal" type="submit" @click="dialog = false" text="Post" color="primary"></v-btn>
                    </v-card-actions>
                </form>
                </v-card>
            </v-dialog>
</template>

<script setup>
import { ref } from 'vue';

const dialog = ref(false)
</script>