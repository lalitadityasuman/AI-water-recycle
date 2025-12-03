<template>
  <div id="app">
    <nav>
      <router-link to="/">Input</router-link> |
      <router-link to="/dashboard">Dashboard</router-link> |
      <router-link to="/history">History</router-link>
    </nav>

    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 20px;
}

nav {
  margin-bottom: 20px;
}

nav a {
  text-decoration: none;
  color: #42b983;
  margin-right: 10px;
}

nav a.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}

main {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
}
</style>
