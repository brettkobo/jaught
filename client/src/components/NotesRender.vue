<template>
  <div class="row'">
    <div class="card-columns">
        <div class="card border-secondary" v-for="(detail,index) in notesData" :key="index">
          <div class="card-header d-flex justify-content-between">
            <span>
              {{ detail.title }}
            </span>

            <button class="btn btn-outline-secondary btn-sm"
                    @click="deleteNote"
                    :data-note-id="detail.note_id">
              &times;
            </button>
          </div>
          <div class="card-body">
            <p class="card-text">{{ detail.body }}</p>
          </div>
          <div class="card-footer">
            <span v-for="(tags,index) in detail.tags"
            :key="index" class="badge badge-info mr-2">
            {{ tags.tag }}
            </span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'NotesRender',
  props: {
    notesData: Array,
  },
  data() {
    return {};
  },
  methods: {
    deleteNote(event) {
      const noteId = event.target.getAttribute('data-note-id');
      console.log(noteId);
      const path = `http://localhost:5000/note/${noteId}`;
      axios.delete(path)
        .then((response) => {
          console.log(response);
          this.$emit('rerender-notes');
        }, (error) => {
          console.log(error);
        });
    },
  },
};
</script>
