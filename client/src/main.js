import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faBold, faItalic, faStrikethrough, faUnderline, faCode, faParagraph,
  faListUl, faListOl, faQuoteLeft, faGripLines, faUndo, faRedo,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import App from './App.vue';
import router from './router';
import store from './store';

library.add(faBold, faItalic, faStrikethrough, faUnderline, faCode, faParagraph,
  faListUl, faListOl, faQuoteLeft, faGripLines, faUndo, faRedo);

Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
