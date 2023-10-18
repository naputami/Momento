<template>
     <v-alert
        closable
        :type="status === 'success'? 'success' : 'error'"
        :title="status === 'success'? `${activity} Success`: `${activity} Failed` "
        :text="message"
        max-height="80"
  ></v-alert>
</template>

<script setup>
// eslint-disable-next-line no-unused-vars
const props = defineProps({
    status: String,
    activity: String,
    message: String
});

</script>