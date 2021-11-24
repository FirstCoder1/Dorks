import Vue from 'vue'
import App from './App.vue'

import router from './router';
import store from './store';
import { BootstrapVue } from 'bootstrap-vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faSpinner } from "@fortawesome/free-solid-svg-icons";
import { faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import vueCountryRegionSelect from 'vue-country-region-select'
import { Row, Column, Hidden } from 'vue-grid-responsive';
import axios from 'axios'
import VueAxios from 'vue-axios'


import './assets/scss/main.scss';

library.add(faTwitter, faInstagram, faSpinner);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false
Vue.use(BootstrapVue);
Vue.use(vueCountryRegionSelect);
Vue.component('row', Row);
Vue.component('column', Column);
Vue.component('hidden', Hidden);
Vue.use(VueAxios, axios)


// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*';

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
