# Lesson 01 Introduction to Next.js Framework

Next.js is a popular open-source React framework developed by Vercel that simplifies the process of building modern web applications. It provides a robust set of tools and features for building server-rendered, statically generated, or hybrid React applications. With its focus on performance, scalability, and developer experience, Next.js has become one of the most widely adopted frameworks for full-stack React development.

## Introduction to Next.js
Next.js is built on top of React, leveraging its component-based architecture while adding advanced features like server-side rendering (SSR), static site generation (SSG), and API routes. It bridges the gap between frontend and backend development, enabling developers to build universal (isomorphic) applications that are both performant and SEO-friendly.

## Key Advantages of Next.js
- **Server-Side Rendering (SSR)**: Pre-renders pages on the server, improving performance and SEO.
- **Static Site Generation (SSG)**: Generates static HTML files at build time, ideal for content-heavy websites.
- **Incremental Static Regeneration (ISR)**: Updates static pages without rebuilding the entire site.
- **File-Based Routing**: Simplifies routing with a file-based system, eliminating the need for complex configuration.
- **API Routes**: Allows developers to create backend APIs directly within the Next.js project.
- **Built-In CSS Support**: Supports CSS modules, styled-jsx, and modern styling solutions.
- **Image Optimization**: Automatically optimizes images using the <Image> component.

## Main Features

| Feature                     | Description                                                                                   | Use Case                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Server-Side Rendering**   | Pre-renders pages on the server for faster load times and improved SEO.                       | Building dynamic websites with real-time data.                          |
| **Static Site Generation**  | Generates static HTML files at build time for fast and scalable applications.                  | Blogs, marketing sites, or documentation portals.                        |
| **Incremental Static Regeneration** | Updates static pages without rebuilding the entire site.                               | Frequently updated content like news articles or product listings.       |
| **File-Based Routing**      | Automatically generates routes based on the `pages` directory structure.                      | Simplifying routing without configuration.                              |
| **API Routes**              | Allows developers to create backend APIs directly within the `pages/api` folder.              | Building RESTful APIs or handling backend logic in a full-stack app.     |
| **Image Optimization**      | Automatically optimizes images using the `<Image>` component.                                 | Delivering responsive and optimized images for better performance.       |
| **Middleware**              | Executes code before a request is completed, enabling advanced routing and security controls. | Redirects, authentication, or A/B testing.                               |
| **TypeScript Support**      | Built-in support for TypeScript for type-safe development.                                    | Large-scale applications requiring strict type-checking.                |
| **Fast Refresh**            | Instantly updates the UI when code changes are made during development.                       | Improving developer productivity with live feedback.                    |
| **Built-In CSS Support**    | Supports CSS Modules, styled-jsx, and modern styling solutions like Tailwind CSS.             | Styling components and pages consistently across the app.               |
| **Internationalized Routing** | Provides built-in support for internationalization (i18n) with locale-based routing.          | Multi-language websites catering to global audiences.                   |
| **Edge Runtime**            | Enables deploying pages and API routes to the edge for ultra-fast global performance.         | High-performance applications requiring low latency worldwide.           |
| **React Server Components** | Renders components on the server while maintaining interactivity and reducing client-side JS. | Building modern apps with reduced bundle sizes and faster rendering.    |


## App Router vs Pages Router

| Feature                          | **Pages Router**                                                                                     | **App Router**                                                                                         |
|----------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Introduction**                 | Traditional routing system introduced in early versions of Next.js.                                 | Introduced in Next.js 13, based on the `app` directory and leveraging React Server Components.         |
| **Directory Structure**          | Routes are defined in the `pages` directory.                                                        | Routes are defined in the `app` directory with support for nested layouts and route groups.            |
| **Routing Mechanism**            | File-based routing: Each file corresponds to a route (e.g., `pages/about.js` → `/about`).           | File-based routing with advanced conventions like `page.js`, `layout.js`, `loading.js`, and `error.js`.|
| **Nested Layouts**               | Requires manual implementation using wrapper components.                                            | Built-in support for nested layouts via `layout.js` files.                                            |
| **Error Handling**               | Manual error handling using try-catch or custom error boundaries.                                   | Built-in error handling with `error.js` files for fallback UI.                                        |
| **Loading States**               | Requires manual implementation using libraries like React Query or SWR.                             | Built-in loading states with `loading.js` files.                                                      |
| **Data Fetching**                | Uses `getStaticProps`, `getServerSideProps`, and `getStaticPaths` for data fetching.                | Simplified data fetching using the `fetch` API with caching, and React Server Components.             |
| **React Server Components**      | Not supported.                                                                                      | Fully supports React Server Components, enabling server-side rendering with reduced client-side JS.   |
| **Streaming & Partial Hydration**| Not supported.                                                                                      | Supports streaming and partial hydration for improved performance.                                    |
| **Route Groups**                 | Not supported.                                                                                      | Supports route groups for organizing routes without affecting URL structure.                          |
| **API Routes**                   | Defined in the `pages/api` directory.                                                               | Can be defined in the `app` directory using `route.js` files.                                         |
| **Middleware**                   | Supported globally using `middleware.js`.                                                           | Middleware works seamlessly with the App Router for advanced routing and security controls.           |
| **Dynamic Routes**               | Supported using square brackets (e.g., `pages/blog/[slug].js`).                                      | Supported using square brackets (e.g., `app/blog/[slug]/page.js`).                                    |
| **Performance Optimization**     | Limited optimizations; relies on SSR and SSG.                                                       | Advanced optimizations like streaming, partial hydration, and automatic caching.                      |
| **Migration Path**               | Fully supported and will remain so for the foreseeable future.                                      | Can coexist with the Pages Router during migration by introducing the `app` directory.                |
| **Use Case**                     | Best for small to medium-sized projects or simpler applications.                                    | Ideal for large-scale, complex applications requiring modern features and scalability.                |
| **Learning Curve**               | Easier to learn and use due to its simplicity.                                                      | Steeper learning curve due to advanced features and new conventions.                                  |
| **Future Support**               | Still supported but considered legacy for new projects.                                             | The future of Next.js routing, actively developed and recommended for new projects.                   |
