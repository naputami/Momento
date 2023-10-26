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


const {addTextOnlyPost, addWithImagePost} = usePostStore();

const formData = reactive({
    content: '',
    file: ''
})

const handleAddPost = async () => {
    if(formData.file === ''){
        const content = {
            'content': formData.content
        }

        await addTextOnlyPost(content)
        console.log('Post without file')
    } else {
        console.log(formData)
        const post = {
            'content': formData.content,
            'file': formData.file[0]
        }
        await addWithImagePost(post)
        console.log('Post with file')
    }
  
}



const dialog = ref(false)
</script>