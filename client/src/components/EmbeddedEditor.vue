<template>
  <div class="editor">
    <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
      <div class="menubar d-flex justify-content-center pt-2 pb-2">

        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.bold() }"
          @click="commands.bold">
          <font-awesome-icon icon="bold"/>
        </button>

<!--
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
          <font-awesome-icon icon="italic" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        >
         <font-awesome-icon icon="strikethrough" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
          <font-awesome-icon icon="underline" />
        </button>
-->
        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.code() }"
          @click="commands.code"
        >
          <font-awesome-icon icon="code" />
        </button>
<!--
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.paragraph() }"
          @click="commands.paragraph"
        >
          <font-awesome-icon icon="paragraph" />
        </button>
-->
        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          <font-awesome-icon icon="list-ul" />
        </button>

        <button
          class="menubar__button notes-form"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          <font-awesome-icon icon="list-ol" />
        </button>
<!--
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.blockquote() }"
          @click="commands.blockquote"
        >
          <font-awesome-icon icon="quote-left" />
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code_block() }"
          @click="commands.code_block"
        >
          <font-awesome-icon icon="code" />
        </button>
-->
        <button
          class="menubar__button notes-form"
          @click="commands.horizontal_rule"
        >
          <font-awesome-icon icon="grip-lines" />
        </button>

        <button
          class="menubar__button notes-form"
          @click="commands.undo"
        >
         <font-awesome-icon icon="undo" />
        </button>

        <button
          class="menubar__button notes-form"
          @click="commands.redo"
        >
          <font-awesome-icon icon="redo" />
        </button>

      </div>
    </editor-menu-bar>

    <editor-content class="editor__content pl-2" :editor="editor" />

  </div>
</template>

<script>
import { Editor, EditorContent, EditorMenuBar } from 'tiptap';
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  HorizontalRule,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History,
} from 'tiptap-extensions';

export default {
  name: 'EmbeddedEditor',
  components: {
    EditorContent,
    EditorMenuBar,

  },
  data() {
    return {
      editor: new Editor({
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
        content: `
        Content...
        `,
        onUpdate: ({ getHTML }) => {
          this.rawContent = getHTML();
          // console.log(this.rawContent);
          this.$emit('contentUp', this.rawContent);
        },
      }),
      rawContent: '',
    };
  },
  methods: {
    alertContent() {
      console.log(this.editor.getHTML());
      this.$emit('contentUp', this.editor.getHTML());
    },
  },
  beforeDestroy() {
    this.editor.destroy();
  },
};
</script>

<style>
.notes-form {
  border-radius: 5px;
  border-color: light;
}
</style>
