<template>
    <div class="purchase-redirect">

    </div>
</template>

<script>
export default {
    name: "PurchaseRedirect",
    mounted() {
        this.$router.push('/purchase/myself');
    }
}
</script>
