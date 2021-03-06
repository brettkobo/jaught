import Vue from 'vue';
import Router from 'vue-router';
import Notes from './components/Notes.vue';
import EmbeddedEditor from './components/EmbeddedEditor.vue';
import NoteModal from './components/NoteModal.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/notes',
      name: 'Notes',
      component: Notes,
    },
    {
      path: '/embed-editor',
      name: 'EmbeddedEditor',
      component: EmbeddedEditor,
    },
    {
      path: '/note-top',
      name: 'NotesModal',
      component: NoteModal,
    },
  ],
});
