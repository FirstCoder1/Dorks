<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>

import data_api from './store/data_api';

export default {
    name: 'App',
    components: {

    },
    mounted() {
        let self = this;
        let state = this.$store.getters.get_state;
        data_api.get_session().then(resp => {
            resp.json().then(data => {
                console.log(data)
                if (data.hasOwnProperty("first_name") && data.hasOwnProperty('email') && data.hasOwnProperty("last_name")) {
                    self.$store.commit('purchase_form', data);
                }
                if (data.hasOwnProperty("to_email") && data.hasOwnProperty("to_name") && data.hasOwnProperty("to_message")) {
                    self.$store.commit('gift_form', data);
                }
                if (data.hasOwnProperty("form_active")) {
                    self.$store.commit("set_form_active", data.form_active);
                }
            })
        })
    }
}
</script>

