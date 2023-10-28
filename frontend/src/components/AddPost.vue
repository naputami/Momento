<template>
      <v-btn @click="dialog = true" icon="$pencil" color="secondary" size="x-large"> </v-btn>

        <v-dialog v-model=dialog width="500">
                <v-card title="Add New Post">
                <v-divider></v-divider>
                <form width="w-100" class="mt-5 pa-5" @submit.prevent="handleAddPost">
                    <v-file-input
                    chips
                    multiple
                    label="Add image (optional)"
                    variant="outlined"
                    prepend-icon="$camera"
                    v-model="formData.file"
                    ></v-file-input>
                    <v-textarea
                    label="Write your thougts here"
                    prepend-icon="$text"
                    variant="outlined"
                    v-model="formData.content"
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
import { ref, reactive } from 'vue';
import { usePostStore } from '../store/usePostStore';
import { useFetch } from '../compostable/post';
import { storeToRefs } from "pinia";



const {data, postTextOnly, postFile} = useFetch();
const store = usePostStore();
const {postState} = storeToRefs(store);
const {setNewPost} = store;

const formData = reactive({
    content: '',
    file: ''
})

const handleAddPost = async () => {
    if(formData.file === ''){
        const content = {
            'content': formData.content
        }

        await postTextOnly('api/posts', content);
        setNewPost(data.value);
        formData.content = ''
        console.log('Post without file')
        console.log('this is post state', postState.value.posts)
    } else {
        const post = {
            'content': formData.content,
            'file': formData.file[0]
        }
        await postFile('api/posts', post);
        setNewPost(data.value);
        formData.content = '';
        formData.file = '';
        console.log('Post with file')
        console.log('this is post state', postState.value.posts)
    }
  
}



const dialog = ref(false)
</script>