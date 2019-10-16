<template>
<form method="post">
  <v-app>
    <v-card width="600" class="mx-auto mt-5">
      <v-card-title>
      <h1 class="display-1">🤩 Sentiment 2 Emoji 🤩</h1>
      
      </v-card-title>
      <v-card-text>
        Use machine learning to predict the emotion sentiment for your supplied text. This model was trained with data from EmoTxt, please view this link for more information about the data or project: <a href="https://arxiv.org/abs/1708.03892">EmoTxt</a> 
        <v-textarea v-model="snippet" prepend-icon="mdi-cards-heart" label="Enter sample text snippet here..." @keyup.enter="submit"/>
      </v-card-text>
    <v-card-actions>
      <v-btn color="success" @click="submit">Submit</v-btn>
      
    </v-card-actions>
    <v-divider></v-divider>
    {{ info }}
  </v-card>
  </v-app>
  </form>
</template>

<script>
import axios from 'axios'
axios.defaults.headers.post['Content-Type'] ='application/x-www-form-urlencoded';

export default {
  name: 'App',
  components: {
  },
  data: () => ({
      info: null,
      snippet: '',
    }),
  methods: {
    async submit () {
      const x = this.snippet;
      const url = 'https://sentiment2emoji.herokuapp.com/api/'.concat(x);
      const r = await axios.post(url);
      this.info = r.data;
    }
  },
};
</script>
