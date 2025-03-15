# Lesson 01 Introduction to Next.js Framework

## React Framework
[React](https://react.dev/) is a powerful, open-source JavaScript library for building user interfaces, particularly single-page applications where data frequently changes. Developed and maintained by Meta (formerly Facebook), React has become one of the most widely adopted frameworks in modern web development due to its component-based architecture , which promotes reusability, modularity, and maintainability. At its core, React uses a declarative programming model , allowing developers to describe how the UI should look based on the application's state, with React efficiently updating the DOM through its virtual DOM mechanism for optimal performance. React supports both functional components and class components , though functional components paired with React Hooks have become the standard for managing state and side effects in a concise and readable manner. With features like JSX (JavaScript XML), developers can write HTML-like syntax directly within JavaScript, making it intuitive to build dynamic UIs. React also integrates seamlessly with state management libraries like Redux or Zustand for global state handling and works well with routing libraries such as React Router for navigation in SPAs. Its unidirectional data flow ensures predictable state updates, while its ecosystem supports server-side rendering (SSR) and static site generation (SSG) via frameworks like Next.js , enabling developers to build SEO-friendly, high-performance applications. React's flexibility extends to mobile development through React Native , allowing developers to build cross-platform mobile apps using the same principles. Backed by a vibrant community, extensive documentation, and a rich ecosystem of tools and libraries, React empowers developers to create scalable, interactive, and responsive applications for a wide range of use cases, from small projects to enterprise-level systems.

## What is Next.js
Next.js is a cutting-edge, open-source React framework developed by Vercel that empowers developers to build high-performance, scalable, and SEO-friendly web applications with ease. Built on top of React, Next.js enhances its capabilities by providing features like server-side rendering (SSR) , static site generation (SSG) , and incremental static regeneration (ISR) , ensuring faster page loads and improved search engine optimization. Its file-based routing system simplifies navigation, while the introduction of the App Router in Next.js 13 revolutionizes routing with support for nested layouts, route groups, and advanced conventions like layout.js, loading.js, and error.js. Next.js also supports API routes , enabling full-stack development by allowing developers to create backend APIs directly within the project. With built-in optimizations such as image optimization , middleware , and edge runtime deployment , Next.js ensures exceptional performance and scalability for modern applications. It seamlessly integrates with TypeScript, CSS frameworks like Tailwind CSS, and databases, making it versatile for both frontend and backend development. Whether building small static websites or large-scale dynamic applications, Next.js offers unparalleled flexibility, performance, and developer experience, solidifying its position as one of the most popular frameworks for modern web development.

## Rendering Strategies
Next.js is renowned for its ability to adapt to various rendering strategies, making it one of the most flexible frameworks for modern web development. Among these strategies, Server-Side Rendering (SSR) , Static Site Generation (SSG) , and Client-Side Rendering (CSR) are the most prominent. Each approach serves a specific purpose and is suited to different use cases, depending on factors like performance, interactivity, and SEO requirements. Let’s explore each in detail:

### 1. Server-Side Rendering (SSR)
**What is SSR?**
Server-Side Rendering (SSR) is a rendering technique where the HTML for a page is generated on the server at request time . When a user visits a page, the server processes the request, fetches the necessary data, generates the HTML, and sends it to the client.

**How Does It Work in Next.js?**
- In Next.js, SSR is implemented using the ```getServerSideProps``` function.
- This function runs on the server for every request, allowing you to fetch data dynamically and pass it as props to your page component.
- The generated HTML is sent to the browser, where React hydrates it to make the page interactive.

```
export async function getServerSideProps(context) {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: { data }, // Pass data to the page component as props
  };
}

export default function Page({ data }) {
  return <div>{data.title}</div>;
}
```

**Use Cases:**
- Applications that require real-time data , such as dashboards, e-commerce platforms with dynamic pricing, or personalized content.
- Pages where SEO is critical, but the data changes frequently (e.g., news websites).

**Advantages:**
- Always serves up-to-date content.
- Excellent for SEO since search engines receive fully rendered HTML.
- Ideal for pages with highly dynamic or user-specific content.

**Disadvantages:**
- Can be slower than SSG because the server must generate the page for every request.
- Higher server load due to frequent data fetching and rendering.

### 2. Static Site Generation (SSG)
**What is SSG?**
Static Site Generation (SSG) is a rendering technique where the HTML for a page is pre-generated at build time . Once generated, the static files can be served directly from a CDN, ensuring blazing-fast performance.

**How Does It Work in Next.js?**
- In Next.js, SSG is implemented using the getStaticProps function.
- During the build process, getStaticProps fetches the required data and generates static HTML files for each page.
- For dynamic routes, the getStaticPaths function specifies which paths should be pre-rendered.

```
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();

  return {
    props: { posts }, // Pass data to the page component as props
  };
}

export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

**Use Cases:**
- Content-heavy websites like blogs, documentation portals, or marketing sites.
- Applications where the data does not change frequently, such as product catalogs or landing pages.

**Advantages:**
- Extremely fast performance since the HTML is pre-built and served via CDN.
- Reduces server load as no computation is required at request time.
- Great for SEO because the fully rendered HTML is available immediately.

**Disadvantages:**
- Not suitable for pages with frequently changing or user-specific content.
- Requires rebuilding the site to update static content unless combined with Incremental Static Regeneration (ISR) .

### 3. Client-Side Rendering (CSR)
**What is CSR?**
Client-Side Rendering (CSR) is a rendering technique where the initial HTML is minimal, and the majority of the content is rendered in the browser using JavaScript. The browser fetches the data and dynamically updates the DOM after the page loads.

```
import { useEffect, useState } from 'react';

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://api.example.com/dashboard')
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  if (!data) return <p>Loading...</p>;

  return <div>{data.content}</div>;
}
```

**Use Cases:**
- Highly interactive applications like dashboards, admin panels, or single-page applications (SPAs).
- Pages where SEO is less important, such as user dashboards or internal tools.

**Advantages:**
- Provides a highly interactive and dynamic user experience.
- Reduces server-side complexity since rendering happens entirely on the client.

**Disadvantages:**
- Slower initial load times because the browser must download and execute JavaScript before rendering the content.
- Poor SEO performance since search engines may struggle to index dynamically rendered content.
- Higher bandwidth usage due to larger JavaScript bundles.

**Incremental Static Regeneration (ISR)**
Next.js introduces a hybrid approach called Incremental Static Regeneration (ISR) , which combines the benefits of SSG and SSR. With ISR, static pages are regenerated in the background after the initial build, ensuring that users always receive up-to-date content without requiring a full rebuild.

**How Does ISR Work?**
- Use the ```revalidate``` option in ```getStaticProps``` to specify how often the page should be updated.
- Example:

```
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();

  return {
    props: { posts },
    revalidate: 60, // Regenerate the page every 60 seconds
  };
}
```

**Advantages:**
- Balances performance and data freshness.
- Reduces the need for frequent full builds.



**How Does It Work in Next.js?**
- CSR is typically used for parts of the application that do not require SEO or immediate rendering.
- Data fetching happens on the client side using hooks like useEffect or libraries like SWR or React Query.
- While Next.js supports CSR, it is often combined with SSR or SSG for better performance and SEO.


## Key Advantages of Next.js
- **Server-Side Rendering (SSR)**: Pre-renders pages on the server, improving performance and SEO.
- **Static Site Generation (SSG)**: Generates static HTML files at build time, ideal for content-heavy websites.
- **Incremental Static Regeneration (ISR)**: Updates static pages without rebuilding the entire site.
- **File-Based Routing**: Simplifies routing with a file-based system, eliminating the need for complex configuration.
- **API Routes**: Allows developers to create backend APIs directly within the Next.js project.
- **Built-In CSS Support**: Supports CSS modules, styled-jsx, and modern styling solutions.
- **Image Optimization**: Automatically optimizes images using the <Image> component.

## Main Features

Next.js is a versatile React framework that provides a comprehensive set of features for building modern web applications. Its **routing structure** is file-based, with the `pages` directory defining routes automatically, while the newer **App Router** introduces advanced conventions like nested layouts and route groups using the `app` directory. **Layouts** are a key feature, allowing developers to create reusable UI structures; the App Router simplifies this with built-in support for nested layouts via `layout.js` files, whereas the Pages Router requires manual implementation. For **data fetching**, Next.js offers multiple methods: the Pages Router uses `getStaticProps`, `getServerSideProps`, and `getStaticPaths`, while the App Router leverages React Server Components and the `fetch` API with caching for streamlined data handling. **Nested routes** are natively supported in the App Router, enabling complex, hierarchical structures, whereas the Pages Router achieves nesting through subdirectories. **Error handling** is another area where the App Router shines, providing automatic fallback UIs with `error.js` files, compared to the manual error boundaries required in the Pages Router. In terms of **performance and scalability**, the App Router introduces modern optimizations like streaming, partial hydration, and edge deployment, making it ideal for large-scale applications, while the Pages Router remains suitable for simpler projects. Finally, the **migration path** from the Pages Router to the App Router is flexible, allowing both systems to coexist during the transition by introducing the `app` directory alongside the `pages` directory. This ensures backward compatibility and a smooth adoption of Next.js's latest advancements. Together, these features make Next.js a robust framework capable of handling projects of any size and complexity.



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

## Why APIs with Next.js

APIs play a crucial role in modern web development, and when combined with Next.js, they enable developers to build powerful, full-stack applications seamlessly. Next.js provides built-in support for **API routes**, allowing developers to create backend functionality directly within the same project as the frontend. This eliminates the need for a separate backend server, simplifying the development process and reducing complexity. With API routes, developers can handle tasks like authentication, database interactions, form submissions, and third-party integrations efficiently. Additionally, Next.js APIs can be deployed to the **Edge Runtime**, ensuring ultra-fast global performance by running code closer to users. This integration of APIs with Next.js not only streamlines the development workflow but also ensures scalability, security, and flexibility, making it an ideal choice for building dynamic, data-driven applications. Whether you're building a small project or a large-scale application, Next.js APIs empower developers to deliver robust, end-to-end solutions with minimal overhead.



