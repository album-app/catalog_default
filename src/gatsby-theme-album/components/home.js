import React from "react"
import { StaticImage } from "gatsby-plugin-image"

const Home = () => {
  return (
    <div>
        <StaticImage className="logo" src="../images/album-default-catalog-landing.png" alt="An album with pictures of different scales and the writing \"everything is a solution\"."/>
    </div>
  )
}

export default Home
