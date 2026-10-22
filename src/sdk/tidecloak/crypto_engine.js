/**
 * UNRELEASED — TideCloak Crypto Engine
 * Standard Web Crypto API & Node.js Crypto implementation for AES-256-GCM chunk encryption.
 */

const crypto = require('crypto');

class CryptoEngine {
  /**
   * Encrypt a plaintext buffer/string with AES-256-GCM using a temporary session key.
   * @param {Buffer|string} plaintext 
   * @param {Buffer} key 32-byte AES key
   * @returns {{ ciphertext: string, iv: string, tag: string }}
   */
  static encryptChunk(plaintext, key) {
    const iv = crypto.randomBytes(12); // Standard 96-bit IV for GCM
    const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
    
    let encrypted = cipher.update(plaintext, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    const tag = cipher.getAuthTag().toString('hex');

    return {
      ciphertext: encrypted,
      iv: iv.toString('hex'),
      tag: tag
    };
  }

  /**
   * Decrypt an AES-256-GCM ciphertext using the emergent ephemeral key.
   * @param {string} ciphertextHex 
   * @param {Buffer} key 32-byte AES key
   * @param {string} ivHex 
   * @param {string} tagHex 
   * @returns {string} Plaintext string/stream buffer
   */
  static decryptChunk(ciphertextHex, key, ivHex, tagHex) {
    const decipher = crypto.createDecipheriv('aes-256-gcm', key, Buffer.from(ivHex, 'hex'));
    decipher.setAuthTag(Buffer.from(tagHex, 'hex'));

    let decrypted = decipher.update(ciphertextHex, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    return decrypted;
  }
}

module.exports = CryptoEngine;
