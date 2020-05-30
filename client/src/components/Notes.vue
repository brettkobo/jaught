<template>
  <div>
    <div class="row mb-4">
      <div class="col-3"></div>
       <div class="col-6">
        <b-form @submit="addNote" @reset="clearForm" v-if="show">
          <b-form-group  id="input-group-1"  label="Title:" label-for="input-1" label-cols-lg="2">
            <b-form-input id="input-1" v-model="form.title" required placeholder="title"/>
          </b-form-group>

          <b-form-group id="input-group-2" label="Note:" label-for="input-2" label-cols-lg="2">
            <b-form-input id="input-2" v-model="form.body" required placeholder="body"/>
          </b-form-group>

          <b-form-group id="input-group-3" label="Tags" label-for="input-3" label-cols-lg="2">
            <b-form-tags input-id="tags-basic"
                         v-model="tags"
                         size="sm"
                         class="mb-2"
                         tag-variant="info"
                         tag-pills
            ></b-form-tags>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
       </div>
      <div class="col-3"></div>
    </div>

    <div>
      <NotesRender @rerender-notes="getAllNotes()" :notesData="notesData"></NotesRender>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
import NotesRender from './NotesRender.vue';

export default {
  components: {
    NotesRender,
  },
  name: 'Notes',
  data() {
    return {
      form: {
        title: '',
        body: '',
        tags: '',
      },
      notesData: [],
      tags: [],
      show: true,
    };
  },
  methods: {
    printTest() {
      console.log('wow this event emit acually worked asdasd');
    },
    clearForm() {
      this.form.title = '';
      this.form.body = '';
      this.tags = []

    },
    getAllNotes() {
      const path = 'http://127.0.0.1:5000/note/all';

      const tempStore = [];
      axios.get(path)
        .then((response) => {
          console.log(response);

          const tempData = response.data.items;
          tempData.forEach((obj) => {
            tempStore.push({
              note_id: obj.note_id,
              title: obj.title,
              body: obj.body,
              tags: JSON.parse(obj.tags),
              collection_id: obj.collection_id,
              creation_date: obj.creation_date,
              modified_date: obj.modified_date,
            });
            console.log(tempStore);
          });

          this.notesData = tempStore;
        });
    },
    addNote(evt) {
      evt.preventDefault();
      const path = 'http://127.0.0.1:5000/note/new';

      const tagTemp = [];

      this.tags.forEach((obj) => { tagTemp.push({ tag: obj }); });

      const rawNote = {
        title: this.form.title,
        body: this.form.body,
        tags: tagTemp,
      };
      axios.post(path, rawNote)
        .then((response) => {
          console.log(response);
          this.getAllNotes();
          this.clearForm();
        }, (error) => {
          console.log(error);
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
