





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-bedfc518345498ab3204d330c1727cde7e733526a09cd7df6867f6a231565091.css" integrity="sha256-vt/FGDRUmKsyBNMwwXJ83n5zNSagnNffaGf2ojFWUJE=" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-9834cae963e0a4ec36c8876cf08b39d02a74cc617a90cc783ed862209e00fc9b.css" integrity="sha256-mDTK6WPgpOw2yIds8Is50Cp0zGF6kMx4PthiIJ4A/Js=" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>docopt/README.rst at master · docopt/docopt</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars0.githubusercontent.com/u/1820478?v=4&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="docopt/docopt" property="og:title" /><meta content="https://github.com/docopt/docopt" property="og:url" /><meta content="docopt - Pythonic command line arguments parser, that will make you smile" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjA0MzI5MzExOjg0MmNjZTdkMzNhYjk5OTc2ZDFiY2I4NzZiNGUxMDBkZDQ1MzI2MTNhOTBhYmI0OTc1NzA2MDZjMGVlOTM3OTY=--a260571383c1a1c6171ea4df48be035959548663">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="883B:1717C:2A129C8:4AA9D4F:59B92FE0" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="883B:1717C:2A129C8:4AA9D4F:59B92FE0" name="octolytics-dimension-request_id" /><meta content="iad" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="31803584" name="octolytics-actor-id" /><meta content="giuseppe-dandrea" name="octolytics-actor-login" /><meta content="463cc5221a6f2e1b80a87874ef0ed29c61e5bdf9f29f53afebeac476898d5801" name="octolytics-actor-hash" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="giuseppe-dandrea">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="MDFjZTAxNjdiMDAzMTg5YjIxZjI4ZGY5ODgwNTU0YjFkZGVlNmIwOWIyMDI4MDIyMDY4YWZiMmQzNmVmNGU2Znx7InJlbW90ZV9hZGRyZXNzIjoiOTMuMzYuMTY1LjE5IiwicmVxdWVzdF9pZCI6Ijg4M0I6MTcxN0M6MkExMjlDODo0QUE5RDRGOjU5QjkyRkUwIiwidGltZXN0YW1wIjoxNTA1MzA4NjUwLCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="UNIVERSE_BANNER">

  <meta name="html-safe-nonce" content="3afc749b9d88eee738cc79fb2bd1b4d6f062f3c2">

  <meta http-equiv="x-pjax-version" content="a018121dc1b3f1b71aabff9528b49c0b">
  

      <link href="https://github.com/docopt/docopt/commits/master.atom" rel="alternate" title="Recent Commits to docopt:master" type="application/atom+xml">

  <meta name="description" content="docopt - Pythonic command line arguments parser, that will make you smile">
  <meta name="go-import" content="github.com/docopt/docopt git https://github.com/docopt/docopt.git">

  <meta content="1820478" name="octolytics-dimension-user_id" /><meta content="docopt" name="octolytics-dimension-user_login" /><meta content="3959394" name="octolytics-dimension-repository_id" /><meta content="docopt/docopt" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="3959394" name="octolytics-dimension-repository_network_root_id" /><meta content="docopt/docopt" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/docopt/docopt/blob/master/README.rst" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex px-3 flex-justify-between container-lg">
    <div class="d-flex flex-justify-between">
      <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/docopt/docopt/search" class="js-site-search-form" data-scoped-search-url="/docopt/docopt/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/docopt/docopt/blob/master/README.rst" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
                Pull requests
</a>            </li>
            <li>
              <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
                Issues
</a>            </li>
                <li>
                  <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container js-header-notifications">
    <span class="d-inline-block  px-2">
      

    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg aria-hidden="true" class="octicon octicon-plus float-left mr-1 mt-1" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="docopt/docopt">This repository</span>
  </div>
    <a class="dropdown-item" href="/docopt/docopt/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@giuseppe-dandrea" class="avatar float-left mr-1" src="https://avatars1.githubusercontent.com/u/31803584?v=4&amp;s=40" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">giuseppe-dandrea</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/giuseppe-dandrea" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/giuseppe-dandrea?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your Gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="GcLWwhNPquMJW82l8XHvQUiGjWHuo4H1IyiQu/Jw/fWj1M1Wlq7WAlFuB25MIrgJXZFEdGZO/+D7WQFr1oQ1bg==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="reW3Qd7qeOM7ib4kE6CRJeLzP4XjAmoCEW4dmeSb+I8X86zVWwsEAmO8dO+u88Zt9+T2kGvvFBfJH4xJwG8wFA==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>


      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



  



    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
      <div class="container repohead-details-container">

        <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="y5OUQ/HfXlvNtwIvwTtURi9c5Dn9PoFH15PRhf77ngwrgMfKsdCAZD9NFxquEIiTsxdv2A+YRu2K5NDnnpi0DQ==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="3959394" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/docopt/docopt/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
            <a class="social-count js-social-count"
              href="/docopt/docopt/watchers"
              aria-label="182 users are watching this repository">
              182
            </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/docopt/docopt/unstar" class="starred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="8l95YAnSKBYv7JRrZZynijrhPUZYV1x2sdpqYyrMLUoT3PKAc7a4irxUJgMDalwjPAyWGJ7N4Fdefei9eKyceg==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar docopt/docopt"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/docopt/docopt/stargazers"
           aria-label="5380 users starred this repository">
          5,380
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/docopt/docopt/star" class="unstarred" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="xMqRtQg2I42Fk8dsE39KzYfbokLNT/qxqW/zYmwuQssEe6BZ7I2N0acedJ2EcJ1TwxeXZtC8xRQPDhhDfiiYQA==" /></div>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star docopt/docopt"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/docopt/docopt/stargazers"
           aria-label="5380 users starred this repository">
          5,380
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of docopt/docopt to your account"
              aria-label="Fork your own copy of docopt/docopt to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/docopt/docopt/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" />
            </include-fragment>
          </div>

    <a href="/docopt/docopt/network" class="social-count"
       aria-label="440 users forked this repository">
      440
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/docopt" class="url fn" rel="author">docopt</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/docopt/docopt" data-pjax="#js-repo-pjax-container">docopt</a></strong>

</h1>

      </div>
      <div class="container">
        
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/docopt/docopt" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /docopt/docopt" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/docopt/docopt/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /docopt/docopt/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">176</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/docopt/docopt/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /docopt/docopt/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">28</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/docopt/docopt/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /docopt/docopt/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <div class="reponav-dropdown js-menu-container">
      <button type="button" class="btn-link reponav-item reponav-dropdown js-menu-target " data-no-toggle aria-expanded="false" aria-haspopup="true">
        Insights
        <svg aria-hidden="true" class="octicon octicon-triangle-down v-align-middle text-gray" height="11" version="1.1" viewBox="0 0 12 16" width="8"><path fill-rule="evenodd" d="M0 5l6 6 6-6z"/></svg>
      </button>
      <div class="dropdown-menu-content js-menu-content">
        <div class="dropdown-menu dropdown-menu-sw">
          <a class="dropdown-item" href="/docopt/docopt/pulse" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
            Pulse
          </a>
          <a class="dropdown-item" href="/docopt/docopt/graphs" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
            Graphs
          </a>
        </div>
      </div>
    </div>
</nav>

      </div>
    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/docopt/docopt/blob/a093f938b7f26564434f3c15a1dcc39e017ad638/README.rst" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:7c2f4d6166ff76244b322b658c4b4b0e -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/0.6.x/README.rst"
               data-name="0.6.x"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                0.6.x
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/call-module/README.rst"
               data-name="call-module"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                call-module
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/delegation/README.rst"
               data-name="delegation"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                delegation
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/error-messages/README.rst"
               data-name="error-messages"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                error-messages
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/fix-travis-tests/README.rst"
               data-name="fix-travis-tests"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-travis-tests
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/docopt/docopt/blob/master/README.rst"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/moving-tests-to-agnostic/README.rst"
               data-name="moving-tests-to-agnostic"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                moving-tests-to-agnostic
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/docopt/docopt/blob/peg-parser/README.rst"
               data-name="peg-parser"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                peg-parser
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.6.2/README.rst"
              data-name="0.6.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.6.2">
                0.6.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.6.1/README.rst"
              data-name="0.6.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.6.1">
                0.6.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.6.0/README.rst"
              data-name="0.6.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.6.0">
                0.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.5.0/README.rst"
              data-name="0.5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.5.0">
                0.5.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.4.2/README.rst"
              data-name="0.4.2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.4.2">
                0.4.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.4.1/README.rst"
              data-name="0.4.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.4.1">
                0.4.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.4.0/README.rst"
              data-name="0.4.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.4.0">
                0.4.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.3.0/README.rst"
              data-name="0.3.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.3.0">
                0.3.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.2.0/README.rst"
              data-name="0.2.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.2.0">
                0.2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.1.1/README.rst"
              data-name="0.1.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.1.1">
                0.1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/docopt/docopt/tree/0.1.0/README.rst"
              data-name="0.1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.1.0">
                0.1.0
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/docopt/docopt/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/docopt/docopt"><span>docopt</span></a></span></span><span class="separator">/</span><strong class="final-path">README.rst</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/docopt/docopt/commit/e756528be99821575c25080e94f434004626c9d9" data-pjax>
          e756528
        </a>
        <relative-time datetime="2016-04-16T03:47:51Z">Apr 16, 2016</relative-time>
      </span>
      <div>
        <img alt="@mboersma" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/73019?v=4&amp;s=40" width="20" />
        <a href="/mboersma" class="user-mention" rel="contributor">mboersma</a>
          <a href="/docopt/docopt/commit/e756528be99821575c25080e94f434004626c9d9" class="message" data-pjax="true" title="Add badges to README.rst.">Add badges to README.rst.</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>7</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="keleshev" href="/docopt/docopt/commits/master/README.rst?author=keleshev"><img alt="@keleshev" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/619158?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mboersma" href="/docopt/docopt/commits/master/README.rst?author=mboersma"><img alt="@mboersma" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/73019?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="ReneSac" href="/docopt/docopt/commits/master/README.rst?author=ReneSac"><img alt="@ReneSac" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/6010063?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="schmir" href="/docopt/docopt/commits/master/README.rst?author=schmir"><img alt="@schmir" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/40620?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="parlarjb" href="/docopt/docopt/commits/master/README.rst?author=parlarjb"><img alt="@parlarjb" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/9376?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="mgedmin" href="/docopt/docopt/commits/master/README.rst?author=mgedmin"><img alt="@mgedmin" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/159967?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="dankeder" href="/docopt/docopt/commits/master/README.rst?author=dankeder"><img alt="@dankeder" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/1021899?v=4&amp;s=40" width="20" /> </a>


    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@keleshev" height="24" src="https://avatars3.githubusercontent.com/u/619158?v=4&amp;s=48" width="24" />
            <a href="/keleshev">keleshev</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mboersma" height="24" src="https://avatars0.githubusercontent.com/u/73019?v=4&amp;s=48" width="24" />
            <a href="/mboersma">mboersma</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@ReneSac" height="24" src="https://avatars3.githubusercontent.com/u/6010063?v=4&amp;s=48" width="24" />
            <a href="/ReneSac">ReneSac</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@schmir" height="24" src="https://avatars2.githubusercontent.com/u/40620?v=4&amp;s=48" width="24" />
            <a href="/schmir">schmir</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@parlarjb" height="24" src="https://avatars1.githubusercontent.com/u/9376?v=4&amp;s=48" width="24" />
            <a href="/parlarjb">parlarjb</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@mgedmin" height="24" src="https://avatars0.githubusercontent.com/u/159967?v=4&amp;s=48" width="24" />
            <a href="/mgedmin">mgedmin</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@dankeder" height="24" src="https://avatars1.githubusercontent.com/u/1021899?v=4&amp;s=48" width="24" />
            <a href="/dankeder">dankeder</a>
          </li>
      </ul>
    </div>
  </div>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/docopt/docopt/raw/master/README.rst" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/docopt/docopt/blame/master/README.rst" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/docopt/docopt/commits/master/README.rst" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/docopt/docopt/edit/master/README.rst" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="rE+B8W9ifWvu/p7IqlhDFw5X3zsOgPylg2KPJiAKqoHORJJxZiTizE1ba4L4cPZuJeMYHgnrCmlROOyfE6dOtw==" /></div>
          <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
          </button>
</form>        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/docopt/docopt/delete/master/README.rst" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="2omfnn9PWdLt0wjMwjLBwnUMADs0w/LaBymBs+50/rX+N1yqqGM4pOkxxOMI1vKZZNSeVCQuBRedIwPWVJRyWQ==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      468 lines (349 sloc)
      <span class="file-info-divider"></span>
    17.6 KB
  </div>
</div>

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><a name="user-content-docopt-creates-beautiful-command-line-interfaces"></a>
<h2><a id="user-content-docopt-creates-beautiful-command-line-interfaces" class="anchor" href="#docopt-creates-beautiful-command-line-interfaces" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><code>docopt</code> creates <em>beautiful</em> command-line interfaces</h2>
<a href="https://travis-ci.org/docopt/docopt"><img alt="https://travis-ci.org/docopt/docopt.svg?branch=master" src="https://camo.githubusercontent.com/67ba88effef4167313ce0c7c5329f7016764979c/68747470733a2f2f7472617669732d63692e6f72672f646f636f70742f646f636f70742e7376673f6272616e63683d6d6173746572" data-canonical-src="https://travis-ci.org/docopt/docopt.svg?branch=master" style="max-width:100%;"></a>
<a href="https://pypi.python.org/pypi/docopt"><img src="https://camo.githubusercontent.com/f494119222add18c6e10e5b8d1f672d2e4b817b9/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646f636f70742e737667" data-canonical-src="https://img.shields.io/pypi/v/docopt.svg" style="max-width:100%;">
</a>
<p>Video introduction to <strong>docopt</strong>: <a href="http://youtu.be/pXhcPJK5cMc">PyCon UK 2012: Create *beautiful*
command-line interfaces with Python</a></p>
<blockquote>
<p>New in version 0.6.1:</p>
<ul>
<li>Fix issue <a href="https://github.com/docopt/docopt/issues/85">#85</a>
which caused improper handling of <code>[options]</code> shortcut
if it was present several times.</li>
</ul>
<p>New in version 0.6.0:</p>
<ul>
<li>New argument <code>options_first</code>, disallows interspersing options
and arguments.  If you supply <code>options_first=True</code> to
<code>docopt</code>, it will interpret all arguments as positional
arguments after first positional argument.</li>
<li>If option with argument could be repeated, its default value
will be interpreted as space-separated list. E.g. with
<code>[default: ./here ./there]</code> will be interpreted as
<code>['./here', './there']</code>.</li>
</ul>
<p>Breaking changes:</p>
<ul>
<li>Meaning of <code>[options]</code> shortcut slightly changed. Previously
it meant <em>"any known option"</em>. Now it means <em>"any option not in
usage-pattern"</em>.  This avoids the situation when an option is
allowed to be repeated unintentionally.</li>
<li><code>argv</code> is <code>None</code> by default, not <code>sys.argv[1:]</code>.
This allows <code>docopt</code> to always use the <em>latest</em> <code>sys.argv</code>,
not <code>sys.argv</code> during import time.</li>
</ul>
</blockquote>
<p>Isn't it awesome how <code>optparse</code> and <code>argparse</code> generate help
messages based on your code?!</p>
<p><em>Hell no!</em>  You know what's awesome?  It's when the option parser <em>is</em>
generated based on the beautiful help message that you write yourself!
This way you don't need to write this stupid repeatable parser-code,
and instead can write only the help message--<em>the way you want it</em>.</p>
<p><strong>docopt</strong> helps you create most beautiful command-line interfaces
<em>easily</em>:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s"><span class="pl-pds">"""</span>Naval Fate.</span>
<span class="pl-s"></span>
<span class="pl-s">Usage:</span>
<span class="pl-s">  naval_fate.py ship new &lt;name&gt;...</span>
<span class="pl-s">  naval_fate.py ship &lt;name&gt; move &lt;x&gt; &lt;y&gt; [--speed=&lt;kn&gt;]</span>
<span class="pl-s">  naval_fate.py ship shoot &lt;x&gt; &lt;y&gt;</span>
<span class="pl-s">  naval_fate.py mine (set|remove) &lt;x&gt; &lt;y&gt; [--moored | --drifting]</span>
<span class="pl-s">  naval_fate.py (-h | --help)</span>
<span class="pl-s">  naval_fate.py --version</span>
<span class="pl-s"></span>
<span class="pl-s">Options:</span>
<span class="pl-s">  -h --help     Show this screen.</span>
<span class="pl-s">  --version     Show version.</span>
<span class="pl-s">  --speed=&lt;kn&gt;  Speed in knots [default: 10].</span>
<span class="pl-s">  --moored      Moored (anchored) mine.</span>
<span class="pl-s">  --drifting    Drifting mine.</span>
<span class="pl-s"></span>
<span class="pl-s"><span class="pl-pds">"""</span></span>
<span class="pl-k">from</span> docopt <span class="pl-k">import</span> docopt


<span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">'</span>__main__<span class="pl-pds">'</span></span>:
    arguments <span class="pl-k">=</span> docopt(<span class="pl-c1">__doc__</span>, <span class="pl-v">version</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">'</span>Naval Fate 2.0<span class="pl-pds">'</span></span>)
    <span class="pl-c1">print</span>(arguments)</pre></div>
<p>Beat that! The option parser is generated based on the docstring above
that is passed to <code>docopt</code> function.  <code>docopt</code> parses the usage
pattern (<code>"Usage: ..."</code>) and option descriptions (lines starting
with dash "<code>-</code>") and ensures that the program invocation matches the
usage pattern; it parses options, arguments and commands based on
that. The basic idea is that <em>a good help message has all necessary
information in it to make a parser</em>.</p>
<p>Also, <a href="http://www.python.org/dev/peps/pep-0257/">PEP 257</a> recommends
putting help message in the module docstrings.</p>
<a name="user-content-installation"></a>
<h2><a id="user-content-installation" class="anchor" href="#installation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Installation</h2>
<p>Use <a href="http://pip-installer.org">pip</a> or easy_install:</p>
<pre>pip install docopt==0.6.2
</pre>
<p>Alternatively, you can just drop <code>docopt.py</code> file into your
project--it is self-contained.</p>
<p><strong>docopt</strong> is tested with Python 2.6, 2.7, 3.3, 3.4, 3.5 and PyPy.</p>
<a name="user-content-testing"></a>
<h2><a id="user-content-testing" class="anchor" href="#testing" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Testing</h2>
<p>You can run unit tests using the command:</p>
<blockquote>
python setup.py test</blockquote>
<a name="user-content-api"></a>
<h2><a id="user-content-api" class="anchor" href="#api" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>API</h2>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> docopt <span class="pl-k">import</span> docopt</pre></div>
<div class="highlight highlight-source-python"><pre>docopt(doc, <span class="pl-v">argv</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">version</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-v">options_first</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</pre></div>
<p><code>docopt</code> takes 1 required and 4 optional arguments:</p>
<ul>
<li><code>doc</code> could be a module docstring (<code>__doc__</code>) or some other
string that contains a <strong>help message</strong> that will be parsed to
create the option parser.  The simple rules of how to write such a
help message are given in next sections.  Here is a quick example of
such a string:</li>
</ul>
<div class="highlight highlight-source-python"><pre><span class="pl-s"><span class="pl-pds">"""</span>Usage: my_program.py [-hso FILE] [--quiet | --verbose] [INPUT ...]</span>
<span class="pl-s"></span>
<span class="pl-s">-h --help    show this</span>
<span class="pl-s">-s --sorted  sorted output</span>
<span class="pl-s">-o FILE      specify output file [default: ./test.txt]</span>
<span class="pl-s">--quiet      print less text</span>
<span class="pl-s">--verbose    print more text</span>
<span class="pl-s"></span>
<span class="pl-s"><span class="pl-pds">"""</span></span></pre></div>
<ul>
<li><p><code>argv</code> is an optional argument vector; by default <code>docopt</code> uses
the argument vector passed to your program (<code>sys.argv[1:]</code>).
Alternatively you can supply a list of strings like <code>['--verbose',
'-o', 'hai.txt']</code>.</p>
</li>
<li><p><code>help</code>, by default <code>True</code>, specifies whether the parser should
automatically print the help message (supplied as <code>doc</code>) and
terminate, in case <code>-h</code> or <code>--help</code> option is encountered
(options should exist in usage pattern, more on that below). If you
want to handle <code>-h</code> or <code>--help</code> options manually (as other
options), set <code>help=False</code>.</p>
</li>
<li><p><code>version</code>, by default <code>None</code>, is an optional argument that
specifies the version of your program. If supplied, then, (assuming
<code>--version</code> option is mentioned in usage pattern) when parser
encounters the <code>--version</code> option, it will print the supplied
version and terminate.  <code>version</code> could be any printable object,
but most likely a string, e.g. <code>"2.1.0rc1"</code>.</p>
<blockquote>
<p>Note, when <code>docopt</code> is set to automatically handle <code>-h</code>,
<code>--help</code> and <code>--version</code> options, you still need to mention
them in usage pattern for this to work. Also, for your users to
know about them.</p>
</blockquote>
</li>
<li><p><code>options_first</code>, by default <code>False</code>.  If set to <code>True</code> will
disallow mixing options and positional argument.  I.e. after first
positional argument, all arguments will be interpreted as positional
even if the look like options.  This can be used for strict
compatibility with POSIX, or if you want to dispatch your arguments
to other programs.</p>
</li>
</ul>
<p>The <strong>return</strong> value is a simple dictionary with options, arguments
and commands as keys, spelled exactly like in your help message.  Long
versions of options are given priority. For example, if you invoke the
top example as:</p>
<pre>naval_fate.py ship Guardian move 100 150 --speed=15
</pre>
<p>the return dictionary will be:</p>
<div class="highlight highlight-source-python"><pre>{<span class="pl-s"><span class="pl-pds">'</span>--drifting<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,    <span class="pl-s"><span class="pl-pds">'</span>mine<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,
 <span class="pl-s"><span class="pl-pds">'</span>--help<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,        <span class="pl-s"><span class="pl-pds">'</span>move<span class="pl-pds">'</span></span>: <span class="pl-c1">True</span>,
 <span class="pl-s"><span class="pl-pds">'</span>--moored<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,      <span class="pl-s"><span class="pl-pds">'</span>new<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,
 <span class="pl-s"><span class="pl-pds">'</span>--speed<span class="pl-pds">'</span></span>: <span class="pl-s"><span class="pl-pds">'</span>15<span class="pl-pds">'</span></span>,        <span class="pl-s"><span class="pl-pds">'</span>remove<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,
 <span class="pl-s"><span class="pl-pds">'</span>--version<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,     <span class="pl-s"><span class="pl-pds">'</span>set<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,
 <span class="pl-s"><span class="pl-pds">'</span>&lt;name&gt;<span class="pl-pds">'</span></span>: [<span class="pl-s"><span class="pl-pds">'</span>Guardian<span class="pl-pds">'</span></span>], <span class="pl-s"><span class="pl-pds">'</span>ship<span class="pl-pds">'</span></span>: <span class="pl-c1">True</span>,
 <span class="pl-s"><span class="pl-pds">'</span>&lt;x&gt;<span class="pl-pds">'</span></span>: <span class="pl-s"><span class="pl-pds">'</span>100<span class="pl-pds">'</span></span>,           <span class="pl-s"><span class="pl-pds">'</span>shoot<span class="pl-pds">'</span></span>: <span class="pl-c1">False</span>,
 <span class="pl-s"><span class="pl-pds">'</span>&lt;y&gt;<span class="pl-pds">'</span></span>: <span class="pl-s"><span class="pl-pds">'</span>150<span class="pl-pds">'</span></span>}</pre></div>
<a name="user-content-help-message-format"></a>
<h2><a id="user-content-help-message-format" class="anchor" href="#help-message-format" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Help message format</h2>
<p>Help message consists of 2 parts:</p>
<ul>
<li><p>Usage pattern, e.g.:</p>
<pre>Usage: my_program.py [-hso FILE] [--quiet | --verbose] [INPUT ...]
</pre>
</li>
<li><p>Option descriptions, e.g.:</p>
<pre>-h --help    show this
-s --sorted  sorted output
-o FILE      specify output file [default: ./test.txt]
--quiet      print less text
--verbose    print more text
</pre>
</li>
</ul>
<p>Their format is described below; other text is ignored.</p>
<a name="user-content-usage-pattern-format"></a>
<h3><a id="user-content-usage-pattern-format" class="anchor" href="#usage-pattern-format" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Usage pattern format</h3>
<p><strong>Usage pattern</strong> is a substring of <code>doc</code> that starts with
<code>usage:</code> (case <em>insensitive</em>) and ends with a <em>visibly</em> empty line.
Minimum example:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s"><span class="pl-pds">"""</span>Usage: my_program.py</span>
<span class="pl-s"></span>
<span class="pl-s"><span class="pl-pds">"""</span></span></pre></div>
<p>The first word after <code>usage:</code> is interpreted as your program's name.
You can specify your program's name several times to signify several
exclusive patterns:</p>
<div class="highlight highlight-source-python"><pre><span class="pl-s"><span class="pl-pds">"""</span>Usage: my_program.py FILE</span>
<span class="pl-s">          my_program.py COUNT FILE</span>
<span class="pl-s"></span>
<span class="pl-s"><span class="pl-pds">"""</span></span></pre></div>
<p>Each pattern can consist of the following elements:</p>
<ul>
<li><strong>&lt;arguments&gt;</strong>, <strong>ARGUMENTS</strong>. Arguments are specified as either
upper-case words, e.g. <code>my_program.py CONTENT-PATH</code> or words
surrounded by angular brackets: <code>my_program.py &lt;content-path&gt;</code>.</li>
<li><strong>--options</strong>.  Options are words started with dash (<code>-</code>), e.g.
<code>--output</code>, <code>-o</code>.  You can "stack" several of one-letter
options, e.g. <code>-oiv</code> which will be the same as <code>-o -i -v</code>. The
options can have arguments, e.g.  <code>--input=FILE</code> or <code>-i FILE</code> or
even <code>-iFILE</code>. However it is important that you specify option
descriptions if you want your option to have an argument, a default
value, or specify synonymous short/long versions of the option (see
next section on option descriptions).</li>
<li><strong>commands</strong> are words that do <em>not</em> follow the described above
conventions of <code>--options</code> or <code>&lt;arguments&gt;</code> or <code>ARGUMENTS</code>,
plus two special commands: dash "<code>-</code>" and double dash "<code>--</code>"
(see below).</li>
</ul>
<p>Use the following constructs to specify patterns:</p>
<ul>
<li><strong>[ ]</strong> (brackets) <strong>optional</strong> elements.  e.g.: <code>my_program.py
[-hvqo FILE]</code></li>
<li><strong>( )</strong> (parens) <strong>required</strong> elements.  All elements that are <em>not</em>
put in <strong>[ ]</strong> are also required, e.g.: <code>my_program.py
--path=&lt;path&gt; &lt;file&gt;...</code> is the same as <code>my_program.py
(--path=&lt;path&gt; &lt;file&gt;...)</code>.  (Note, "required options" might be not
a good idea for your users).</li>
<li><strong>|</strong> (pipe) <strong>mutually exclusive</strong> elements. Group them using <strong>(
)</strong> if one of the mutually exclusive elements is required:
<code>my_program.py (--clockwise | --counter-clockwise) TIME</code>. Group
them using <strong>[ ]</strong> if none of the mutually-exclusive elements are
required: <code>my_program.py [--left | --right]</code>.</li>
<li><strong>...</strong> (ellipsis) <strong>one or more</strong> elements. To specify that
arbitrary number of repeating elements could be accepted, use
ellipsis (<code>...</code>), e.g.  <code>my_program.py FILE ...</code> means one or
more <code>FILE</code>-s are accepted.  If you want to accept zero or more
elements, use brackets, e.g.: <code>my_program.py [FILE ...]</code>. Ellipsis
works as a unary operator on the expression to the left.</li>
<li><strong>[options]</strong> (case sensitive) shortcut for any options.  You can
use it if you want to specify that the usage pattern could be
provided with any options defined below in the option-descriptions
and do not want to enumerate them all in usage-pattern.</li>
<li>"<code>[--]</code>". Double dash "<code>--</code>" is used by convention to separate
positional arguments that can be mistaken for options. In order to
support this convention add "<code>[--]</code>" to your usage patterns.</li>
<li>"<code>[-]</code>". Single dash "<code>-</code>" is used by convention to signify that
<code>stdin</code> is used instead of a file. To support this add "<code>[-]</code>"
to your usage patterns. "<code>-</code>" acts as a normal command.</li>
</ul>
<p>If your pattern allows to match argument-less option (a flag) several
times:</p>
<pre>Usage: my_program.py [-v | -vv | -vvv]
</pre>
<p>then number of occurrences of the option will be counted. I.e.
<code>args['-v']</code> will be <code>2</code> if program was invoked as <code>my_program
-vv</code>. Same works for commands.</p>
<p>If your usage patterns allows to match same-named option with argument
or positional argument several times, the matched arguments will be
collected into a list:</p>
<pre>Usage: my_program.py &lt;file&gt; &lt;file&gt; --path=&lt;path&gt;...
</pre>
<p>I.e. invoked with <code>my_program.py file1 file2 --path=./here
--path=./there</code> the returned dict will contain <code>args['&lt;file&gt;'] ==
['file1', 'file2']</code> and <code>args['--path'] == ['./here', './there']</code>.</p>
<a name="user-content-option-descriptions-format"></a>
<h3><a id="user-content-option-descriptions-format" class="anchor" href="#option-descriptions-format" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Option descriptions format</h3>
<p><strong>Option descriptions</strong> consist of a list of options that you put
below your usage patterns.</p>
<p>It is necessary to list option descriptions in order to specify:</p>
<ul>
<li>synonymous short and long options,</li>
<li>if an option has an argument,</li>
<li>if option's argument has a default value.</li>
</ul>
<p>The rules are as follows:</p>
<ul>
<li><p>Every line in <code>doc</code> that starts with <code>-</code> or <code>--</code> (not counting
spaces) is treated as an option description, e.g.:</p>
<pre>Options:
  --verbose   # GOOD
  -o FILE     # GOOD
Other: --bad  # BAD, line does not start with dash "-"
</pre>
</li>
<li><p>To specify that option has an argument, put a word describing that
argument after space (or equals "<code>=</code>" sign) as shown below. Follow
either &lt;angular-brackets&gt; or UPPER-CASE convention for options'
arguments.  You can use comma if you want to separate options. In
the example below, both lines are valid, however you are recommended
to stick to a single style.:</p>
<pre>-o FILE --output=FILE       # without comma, with "=" sign
-i &lt;file&gt;, --input &lt;file&gt;   # with comma, without "=" sing
</pre>
</li>
<li><p>Use two spaces to separate options with their informal description:</p>
<pre>--verbose More text.   # BAD, will be treated as if verbose option had
                       # an argument "More", so use 2 spaces instead
-q        Quit.        # GOOD
-o FILE   Output file. # GOOD
--stdout  Use stdout.  # GOOD, 2 spaces
</pre>
</li>
<li><p>If you want to set a default value for an option with an argument,
put it into the option-description, in form <code>[default:
&lt;my-default-value&gt;]</code>:</p>
<pre>--coefficient=K  The K coefficient [default: 2.95]
--output=FILE    Output file [default: test.txt]
--directory=DIR  Some directory [default: ./]
</pre>
</li>
<li><p>If the option is not repeatable, the value inside <code>[default: ...]</code>
will be interpreted as string.  If it <em>is</em> repeatable, it will be
splited into a list on whitespace:</p>
<pre>Usage: my_program.py [--repeatable=&lt;arg&gt; --repeatable=&lt;arg&gt;]
                     [--another-repeatable=&lt;arg&gt;]...
                     [--not-repeatable=&lt;arg&gt;]

# will be ['./here', './there']
--repeatable=&lt;arg&gt;          [default: ./here ./there]

# will be ['./here']
--another-repeatable=&lt;arg&gt;  [default: ./here]

# will be './here ./there', because it is not repeatable
--not-repeatable=&lt;arg&gt;      [default: ./here ./there]
</pre>
</li>
</ul>
<a name="user-content-examples"></a>
<h3><a id="user-content-examples" class="anchor" href="#examples" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Examples</h3>
<p>We have an extensive list of <a href="https://github.com/docopt/docopt/tree/master/examples">examples</a> which cover
every aspect of functionality of <strong>docopt</strong>.  Try them out, read the
source if in doubt.</p>
<a name="user-content-subparsers-multi-level-help-and-huge-applications-like-git"></a>
<h3><a id="user-content-subparsers-multi-level-help-and-huge-applications-like-git" class="anchor" href="#subparsers-multi-level-help-and-huge-applications-like-git" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Subparsers, multi-level help and <em>huge</em> applications (like git)</h3>
<p>If you want to split your usage-pattern into several, implement
multi-level help (with separate help-screen for each subcommand),
want to interface with existing scripts that don't use <strong>docopt</strong>, or
you're building the next "git", you will need the new <code>options_first</code>
parameter (described in API section above). To get you started quickly
we implemented a subset of git command-line interface as an example:
<a href="https://github.com/docopt/docopt/tree/master/examples/git">examples/git</a></p>
<a name="user-content-data-validation"></a>
<h3><a id="user-content-data-validation" class="anchor" href="#data-validation" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Data validation</h3>
<p><strong>docopt</strong> does one thing and does it well: it implements your
command-line interface.  However it does not validate the input data.
On the other hand there are libraries like <a href="https://github.com/halst/schema">python schema</a> which make validating data a
breeze.  Take a look at <a href="https://github.com/docopt/docopt/tree/master/examples/validation_example.py">validation_example.py</a>
which uses <strong>schema</strong> to validate data and report an error to the
user.</p>
<a name="user-content-using-docopt-with-config-files"></a>
<h3><a id="user-content-using-docopt-with-config-files" class="anchor" href="#using-docopt-with-config-files" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Using docopt with config-files</h3>
<p>Often configuration files are used to provide default values which
could be overriden by command-line arguments.  Since <strong>docopt</strong>
returns a simple dictionary it is very easy to integrate with
config-files written in JSON, YAML or INI formats.
<a href="/docopt/docopt/blob/master/examples/config_file_example.py">config_file_example.py</a> provides
and example of how to use <strong>docopt</strong> with JSON or INI config-file.</p>
<a name="user-content-development"></a>
<h2><a id="user-content-development" class="anchor" href="#development" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Development</h2>
<p>We would <em>love</em> to hear what you think about <strong>docopt</strong> on our <a href="http://github.com/docopt/docopt/issues">issues
page</a></p>
<p>Make pull requests, report bugs, suggest ideas and discuss
<strong>docopt</strong>. You can also drop a line directly to
&lt;<a href="mailto:vladimir@keleshev.com">vladimir@keleshev.com</a>&gt;.</p>
<a name="user-content-porting-docopt-to-other-languages"></a>
<h2><a id="user-content-porting-docopt-to-other-languages" class="anchor" href="#porting-docopt-to-other-languages" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Porting <code>docopt</code> to other languages</h2>
<p>We think <strong>docopt</strong> is so good, we want to share it beyond the Python
community! All official docopt ports to other languages can be found
under the <a href="http://github.com/docopt">docopt organization page</a>
on GitHub.</p>
<p>If your favourite language isn't among then, you can always create a
port for it! You are encouraged to use the Python version as a
reference implementation.  A Language-agnostic test suite is bundled
with <a href="http://github.com/docopt/docopt">Python implementation</a>.</p>
<p>Porting discussion is on <a href="http://github.com/docopt/docopt/issues">issues page</a>.</p>
<a name="user-content-changelog"></a>
<h2><a id="user-content-changelog" class="anchor" href="#changelog" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Changelog</h2>
<p><strong>docopt</strong> follows <a href="http://semver.org">semantic versioning</a>.  The
first release with stable API will be 1.0.0 (soon).  Until then, you
are encouraged to specify explicitly the version in your dependency
tools, e.g.:</p>
<pre>pip install docopt==0.6.2
</pre>
<ul>
<li>0.6.2 Bugfix release.</li>
<li>0.6.1 Bugfix release.</li>
<li>0.6.0 <code>options_first</code> parameter.
<strong>Breaking changes</strong>: Corrected <code>[options]</code> meaning.
<code>argv</code> defaults to <code>None</code>.</li>
<li>0.5.0 Repeated options/commands are counted or accumulated into a
list.</li>
<li>0.4.2 Bugfix release.</li>
<li>0.4.0 Option descriptions become optional,
support for "<code>--</code>" and "<code>-</code>" commands.</li>
<li>0.3.0 Support for (sub)commands like git remote add.
Introduce <code>[options]</code> shortcut for any options.
<strong>Breaking changes</strong>: <code>docopt</code> returns dictionary.</li>
<li>0.2.0 Usage pattern matching. Positional arguments parsing based on
usage patterns.
<strong>Breaking changes</strong>: <code>docopt</code> returns namespace (for arguments),
not list. Usage pattern is formalized.</li>
<li>0.1.0 Initial release. Options-parsing only (based on options
description).</li>
</ul>

</article>
  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2017 <span title="0.19682s from unicorn-1011525001-8xnhs">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha256-8q4ohCjL4ztV3ECDYeIe1e5DMasRlfxtng0fybFEsEI=" src="https://assets-cdn.github.com/assets/frameworks-f2ae288428cbe33b55dc408361e21ed5ee4331ab1195fc6d9e0d1fc9b144b042.js"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha256-z++Hm3crDoqeaDOimGQpPvMd0jo6K12WjBGLJ6Vx3Vw=" src="https://assets-cdn.github.com/assets/github-cfef879b772b0e8a9e6833a29864293ef31dd23a3a2b5d968c118b27a571dd5c.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

