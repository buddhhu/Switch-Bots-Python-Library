import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Getting started Tutorial - 5min ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main style={{
        padding: "1rem"
      }}>
        {/* <HomepageFeatures /> */}
       <h3 style={{
          marginTop: 10
        }}># Installation</h3>
        <code>
          pip3 install swibots
        </code>
        <h3 style={{
          marginTop: "8px"
        }}>
        # Installing from source
        </h3>
        <code>
          pip3 install git+https://github.com/switchcollab/Switch-Bots-Python-Library.git
        </code>
      </main>
    </Layout>
  );
}
