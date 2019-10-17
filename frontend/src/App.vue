<template>
<form method="post">
  <v-app>

    <v-container>
      <v-layout row justify-space-between>
        <v-flex md6>
          <v-card width="600" class=" mt-5">
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

        </v-flex>
        <v-flex md1>

        </v-flex>
        <v-flex md4>
          <v-card
    color="#26c6da"
    dark
    max-width="400"
    class="mt-5"
  >
    <v-card-title>
      <v-icon
        large
        left
      >
        mdi-twitter
      </v-icon>
      <span class="title font-weight-light">Twitter</span>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      "Collard greens are absolutely disgusting. "
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            src="https://pbs.twimg.com/profile_images/644340637156839424/0PiHdG3e_400x400.jpg"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>Abe Lincoln</v-list-item-title>
        </v-list-item-content>

        <v-row
          align="center"
          justify="end"
        >
          <v-icon class="mr-1">mdi-heart</v-icon>
          <span class="subheading mr-2">999</span>
          <span class="mr-1">·</span>
          <v-icon class="mr-1">mdi-share-variant</v-icon>
          <span class="subheading">-30</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
        </v-flex>
      </v-layout> 
    </v-container>
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
    created() {
      this.$vuetify.theme.dark = true
    },
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
