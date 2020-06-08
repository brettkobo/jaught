<template>
  <div>
    <div class="row mb-4 mt-4">
      <div class="col-3"></div>
       <div class="col-6">
         <div class="d-flex justify-content-center">
           <b-button v-b-modal.new-note class="mr-2">Create Note</b-button>
           <b-button>Organize Notes</b-button>
         </div>
       </div>
      <div class="col-3"></div>
    </div>

      <NoteModal @note-submitted="getAllNotes"></NoteModal>

    <div>
      <NotesRender @rerender-notes="getAllNotes"
                   :notesData="notesData"></NotesRender>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import NotesRender from './NotesRender.vue';
import NoteModal from './NoteModal.vue';

export default {
  components: {
    NotesRender,
    NoteModal,
  },
  name: 'Notes',
  data() {
    return {
      notesData: [],
      show: true,
    };
  },
  methods: {
    getAllNotes() {
      const path = 'http://127.0.0.1:5000/note/all';
      this.notesData = [];
      const tempStore = [];
      axios.get(path)
        .then((response) => {
          const tempData = response.data.items;
          tempData.forEach((obj) => {
            tempStore.push({
              note_id: obj.note_id,
              title: obj.title,
              body: obj.body,
              tags: JSON.parse(obj.tags),
              color: obj.color,
              collection_id: obj.collection_id,
              creation_date: obj.creation_date,
              modified_date: obj.modified_date,
            });
          });

          this.notesData = tempStore;
        });
    },
  },
  created() {
    this.getAllNotes();
  },
};
</script>

<style>
  .close {
    font-size: 1.0rem;
  }
</style>
