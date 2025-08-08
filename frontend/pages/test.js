export default function Test() {
  return (
    <div style={{padding: '20px', fontFamily: 'Arial, sans-serif'}}>
      <h1>🚀 Vercel Test Page</h1>
      <p>If you can see this page, Vercel deployment is working!</p>
      <p>Backend URL: {process.env.NEXT_PUBLIC_BACKEND_URL || 'Not set'}</p>
      <p>Environment: {process.env.NODE_ENV}</p>
    </div>
  );
}