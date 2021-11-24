<template>
    <div class="header">
        <a @click="$router.push('/')">
            <img :src="require('@/assets/img/logo.svg')" alt="">
        </a>
        <div class="header-social">
            <a href="https://www.twitter.com/suchdorks" target="_blank">
                <font-awesome-icon :icon="['fab', 'twitter']" class="fa-lg"></font-awesome-icon>
            </a>
            <a href="https://www.instagram.com/suchdorks" target="_blank">
                <font-awesome-icon :icon="['fab', 'instagram']" class="fa-lg"></font-awesome-icon>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Header"
}
</script>
