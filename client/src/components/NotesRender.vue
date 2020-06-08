<template>
  <div class="row'">
    <div class="card-columns">
        <div class="card shadow"
             v-for="(detail,index) in notesData"
             :key="index">
          <div class="card-header d-flex justify-content-between opposite font-weight-bold"
               v-bind:style="{ 'background-color': detail.color }">

              {{ detail.title }}

            <button class="btn btn-outline-secondary btn-sm"
                    @click="deleteNote"
                    :data-note-id="detail.note_id">
              &times;
            </button>
          </div>

            <NoteBody :body="detail.body"></NoteBody>

          <div class="card-footer" v-bind:style="{ 'background-color': detail.color }">
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
import NoteBody from './NotesBody.vue';

export default {
  name: 'NotesRender',
  components: {
    NoteBody,
  },
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

<style>
.opposite {
/*sets the background for the base class*/
    background: rgb(var(--red), var(--green), var(--blue));

  --r: calc(var(--red) * 0.2126);
  --g: calc(var(--green) * 0.7152);
  --b: calc(var(--blue) * 0.0722);
  --sum: calc(var(--r) + var(--g) + var(--b));

  --perceived-lightness: calc(var(--sum) / 255);


  color: hsl(0, 0%, calc((var(--perceived-lightness) - var(--threshold)) * -10000000%));


 --border-alpha: calc((var(--perceived-lightness) - var(--border-threshold)) * 100);
}
</style>
