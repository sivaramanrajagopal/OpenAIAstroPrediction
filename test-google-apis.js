#!/usr/bin/env node
/**
 * Test script for Google APIs integration
 * Run with: node test-google-apis.js
 * 
 * This script tests the server-side API routes to ensure Google APIs are working correctly.
 */

const https = require('https');
const http = require('http');

// Test configuration
const BASE_URL = process.env.TEST_URL || 'http://localhost:3000';
const TEST_COORDINATES = {
  chennai: { lat: 13.0827, lng: 80.2707, name: 'Chennai, India' },
  newyork: { lat: 40.7128, lng: -74.0060, name: 'New York, USA' },
  london: { lat: 51.5074, lng: -0.1278, name: 'London, UK' }
};

// Helper function to make HTTP requests
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    const protocol = url.startsWith('https') ? https : http;
    
    protocol.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        try {
          resolve({
            status: res.statusCode,
            data: JSON.parse(data)
          });
        } catch (e) {
          resolve({
            status: res.statusCode,
            data: data
          });
        }
      });
    }).on('error', reject);
  });
}

async function testGoogleApis() {
  console.log('🧪 Testing Google APIs Integration');
  console.log('==================================');
  
  let passedTests = 0;
  let totalTests = 0;
  
  // Test 1: Timezone API
  console.log('\\n1️⃣ Testing Timezone API...');
  for (const [key, coords] of Object.entries(TEST_COORDINATES)) {
    totalTests++;
    try {
      const url = `${BASE_URL}/api/google-timezone?lat=${coords.lat}&lng=${coords.lng}`;
      const result = await makeRequest(url);
      
      if (result.status === 200 && result.data.timezone_id) {
        console.log(`   ✅ ${coords.name}: ${result.data.timezone_id} (offset: ${result.data.total_offset}h)`);
        passedTests++;
      } else {
        console.log(`   ❌ ${coords.name}: Failed - ${result.data.error || 'Unknown error'}`);
      }
    } catch (error) {
      console.log(`   ❌ ${coords.name}: Error - ${error.message}`);
    }
  }
  
  // Test 2: Reverse Geocoding API
  console.log('\\n2️⃣ Testing Reverse Geocoding API...');
  for (const [key, coords] of Object.entries(TEST_COORDINATES)) {
    totalTests++;
    try {
      const url = `${BASE_URL}/api/google-geocode?lat=${coords.lat}&lng=${coords.lng}`;
      const result = await makeRequest(url);
      
      if (result.status === 200 && result.data.results && result.data.results.length > 0) {
        const address = result.data.results[0].formatted_address;
        console.log(`   ✅ ${coords.name}: ${address}`);
        passedTests++;
      } else {
        console.log(`   ❌ ${coords.name}: Failed - ${result.data.error || 'No results'}`);
      }
    } catch (error) {
      console.log(`   ❌ ${coords.name}: Error - ${error.message}`);
    }
  }
  
  // Test 3: Places Search API
  console.log('\\n3️⃣ Testing Places Search API...');
  const searchQueries = ['Chennai', 'New York', 'London', 'Tokyo'];
  for (const query of searchQueries) {
    totalTests++;
    try {
      const url = `${BASE_URL}/api/google-places?query=${encodeURIComponent(query)}`;
      const result = await makeRequest(url);
      
      if (result.status === 200 && result.data.suggestions && result.data.suggestions.length > 0) {
        const topResult = result.data.suggestions[0];
        console.log(`   ✅ "${query}": Found ${result.data.suggestions.length} results (top: ${topResult.description})`);
        passedTests++;
      } else {
        console.log(`   ❌ "${query}": Failed - ${result.data.error || 'No suggestions'}`);
      }
    } catch (error) {
      console.log(`   ❌ "${query}": Error - ${error.message}`);
    }
  }
  
  // Test Summary
  console.log('\\n📊 Test Summary');
  console.log('================');
  console.log(`Total Tests: ${totalTests}`);
  console.log(`Passed: ${passedTests}`);
  console.log(`Failed: ${totalTests - passedTests}`);
  console.log(`Success Rate: ${Math.round((passedTests / totalTests) * 100)}%`);
  
  if (passedTests === totalTests) {
    console.log('\\n🎉 All tests passed! Google APIs are working correctly.');
  } else if (passedTests === 0) {
    console.log('\\n💥 All tests failed. Check your configuration:');
    console.log('   - Is your Next.js server running?');
    console.log('   - Is GOOGLE_API_KEY set in your environment?');
    console.log('   - Are the required Google APIs enabled?');
  } else {
    console.log(`\\n⚠️ Some tests failed. ${passedTests}/${totalTests} APIs are working.`);
  }
  
  // Configuration Check
  console.log('\\n🔧 Configuration Check');
  console.log('=======================');
  console.log(`Base URL: ${BASE_URL}`);
  console.log(`Google API Key: ${process.env.GOOGLE_API_KEY ? '✅ Set' : '❌ Not set'}`);
  
  if (!process.env.GOOGLE_API_KEY) {
    console.log('\\n📝 To fix missing API key:');
    console.log('   1. Get API key from Google Cloud Console');
    console.log('   2. Add to .env.local: GOOGLE_API_KEY=your_key_here');
    console.log('   3. Restart your Next.js server');
  }
}

// Run tests
if (require.main === module) {
  testGoogleApis().catch(console.error);
}

module.exports = { testGoogleApis };