<template>
  <div class="card-body">
    <editor-content :editor="editor"/>
  </div>
</template>

<script>
import { Editor, EditorContent } from 'tiptap';
import {
  Blockquote, Bold,
  BulletList, Code,
  CodeBlock,
  HardBreak,
  Heading, History,
  HorizontalRule, Italic, Link, ListItem, OrderedList, Strike, TodoItem, TodoList, Underline,
} from 'tiptap-extensions';

export default {
  name: 'NoteBody',
  components: {
    EditorContent,
  },
  props: {
    body: String,
  },
  data() {
    return {
      editor: null,
    };
  },
  created() {
    this.editor = new Editor({
      extensions: [
        new Blockquote(),
        new BulletList(),
        new CodeBlock(),
        new HardBreak(),
        new Heading({ levels: [1, 2, 3] }),
        new HorizontalRule(),
        new ListItem(),
        new OrderedList(),
        new TodoItem(),
        new TodoList(),
        new Link(),
        new Bold(),
        new Code(),
        new Italic(),
        new Strike(),
        new Underline(),
        new History(),
      ],
      editable: false,
      content: '',
    });
    this.editor.setContent(this.body);
  },
};
</script>
