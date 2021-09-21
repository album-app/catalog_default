module.exports = {
  pathPrefix: `/catalogs/default`,
  siteMetadata: {
    title: 'album default catalog',
    subtitle: 'solutions available in all album installations',
    catalog_url: 'https://gitlab.com/album-app/catalogs/default',
    menuLinks:[
      {
         name:'Catalog',
         link:'/catalog'
      },
      {
         name:'About',
         link:'/about'
      },
    ]
  },
  plugins: [{ resolve: `gatsby-theme-album`, options: {} }],
}
