import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: null,
        sidenav_open: true,
        form_active: 0,
        purchase_result: '',
        first_name: '',
        last_name: '',
        email: '',
        to_email: '',
        to_name: '',
        to_message: ''
    },

    mutations: {
        set_user(state, user) {
            state.user = user;
        },
        set_form_active(state, btn_active) {
            state.form_active = btn_active;
        },
        purchase_form(state, myself_form) {
            state.first_name = myself_form.first_name;
            state.last_name = myself_form.last_name;
            state.email = myself_form.email;
        },
        gift_form(state, gift_form) {
            state.to_email = gift_form.to_email;
            state.to_name = gift_form.to_name;
            state.to_message = gift_form.to_message;
        },
        update_state(state, payload) {
            for (let key in payload) {
                if (state.hasOwnProperty(key)) {
                    state[key] = payload[key]
                }
            }
        },
        update_first_name(state, first_name) {
            state.first_name = first_name;
        },
        update_last_name(state, last_name) {
            state.last_name = last_name
        },
        update_email(state, email) {
            state.email = email
        }
    },

    actions: {
        logout({commit}) {
            commit('set_user', null);
        },
        login({commit}, user) {
            commit('set_user', user);
        },
    },

    modules: {

    },

    getters: {
        get_form_active(state) {
            return state.form_active;
        },
        get_purchase_form(state) {
            return {first_name: state.first_name, last_name: state.last_name, email: state.email}
        },
        get_gift_form(state) {
            return {to_email: state.to_email, to_name: state.to_name, to_message: state.to_message}
        },
        get_state_exists(state, key) {
            return state.hasOwnProperty(key)
        },
        get_state(state) {
            return state;
        },
        get_email(state) {
            return state.email
        }
    }
})