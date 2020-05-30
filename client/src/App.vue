<template>
  <div class="d-flex" id="wrapper">
      <div class="bg-light border-right" id="sidebar-wrapper">
        <div class="sidebar-heading">Start Bootstrap </div>
        <div class="list-group list-group-flush">
          <a href="/notes" class="list-group-item list-group-item-action bg-light">Notes</a>
          <a href="/organize" class="list-group-item list-group-item-action bg-light">Organize</a>
          <a href="/weather" class="list-group-item list-group-item-action bg-light">Weather</a>
      </div>

    </div>

    <div id="page-content-wrapper">

      <nav class="navbar navbar-light bg-light">
      <a class="navbar-brand" href="#">Jaught</a>
      </nav>

      <div id="app" class="container-fluid">
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style>
  body {
  overflow-x: hidden;
}

#sidebar-wrapper {
  min-height: 100vh;
  margin-left: -15rem;
  -webkit-transition: margin .25s ease-out;
  -moz-transition: margin .25s ease-out;
  -o-transition: margin .25s ease-out;
  transition: margin .25s ease-out;
}

#sidebar-wrapper .sidebar-heading {
  padding: 0.875rem 1.25rem;
  font-size: 1.2rem;
}

#sidebar-wrapper .list-group {
  width: 15rem;
}

#page-content-wrapper {
  min-width: 100vw;
}

#wrapper.toggled #sidebar-wrapper {
  margin-left: 0;
}

@media (min-width: 768px) {
  #sidebar-wrapper {
    margin-left: 0;
  }

  #page-content-wrapper {
    min-width: 0;
    width: 100%;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: -15rem;
  }
}
</style>
