<template>
  <div>
    <b-modal id="new-note"
             ref="new-note"
             content-class="shadow"
             header-class="p-0"
             footer-class="p-0 m-0">
      <!--  hide-backdrop
            header-class="coral"
            footer-class="coral"
       -->

        <template v-slot:modal-header>
          <div class="w-100 h-100 m-0" v-bind:style="{ 'background-color': colors.hex }">.
          </div>
        </template>

      <b-form @submit="addNote" v-if="show">
        <b-form-group>
          <b-form-input id="input-1"
                        placeholder="Title..."
                        maxlength="100"
                        v-model="form.title"/>
        </b-form-group>

        <b-form-group class="border notes-form">
          <EmbeddedEditor @contentUp="form.body = $event"/>
        </b-form-group>

        <b-form-group>
          <b-form-tags class="mb-2"
                       placeholder="Tags..."
                       input-id="tags-basic"
                       tag-pills
                       tag-variant="info"
                       v-model="tags"/>
        </b-form-group>


        <b-form-group>
           <!-- <b-button :pressed.sync="colorShow" variant="info">Color</b-button> -->
            <compact-picker v-model="colors"
                            v-if="colorShow"
                            :palette="[
                            '#ffadad',
                            '#ffd6a5',
                            '#fdffb6',
                            '#caffbf',
                            '#9bf6ff',
                            '#a0c4ff',
                            '#bdb2ff',
                            '#ffc6ff',
                            '#ffee93',
                            '#fcf5c7',
                            '#a0ced9',
                            '#adf7b6'
                            ]"></compact-picker>
        </b-form-group>

        <b-button block type="submit" variant="primary">Submit</b-button>

      </b-form>

      <template v-slot:modal-footer>
        <div class="w-100 h-100 m-0" v-bind:style="{ 'background-color': colors.hex }">.
        </div>
      </template>

    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import { Compact } from 'vue-color';
import EmbeddedEditor from './EmbeddedEditor.vue';


export default {
  name: 'NoteModal',
  components: {
    EmbeddedEditor,
    'compact-picker': Compact,
  },
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
      colorShow: true,
      colors: {
        hex: '#a0c4ff',
      },
    };
  },
  methods: {
    clearForm() {
      this.form.title = '';
      this.form.body = '';
      this.tags = [];
      this.colors.hex = {};
    },
    addNote(evt) {
      evt.preventDefault();
      const path = 'http://127.0.0.1:5000/note/new';

      const tagTemp = [];

      this.tags.forEach((obj) => {
        tagTemp.push({ tag: obj });
      });

      const rawNote = {
        title: this.form.title,
        body: this.form.body,
        tags: tagTemp,
        color: this.colors.hex,
      };
      axios.post(path, rawNote)
        .then(() => {
          this.$refs['new-note'].hide();
          this.$emit('note-submitted');
          this.clearForm();
        }, (error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.coral {
  background-color: coral;
}

.notes-form {
  border-radius: 5px;
  border-color: #ced4da;
}

.modal-backdrop {
    opacity:0.5 !important;
}
.form-control::-webkit-input-placeholder {
  color: black;
}

::placeholder {
  color: black;
}

</style>
